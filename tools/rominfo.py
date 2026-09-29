#!/usr/bin/env python3
"""Identifie une ROM GBA : lit l'en-tête, vérifie son checksum et calcule les empreintes.

Usage :
    python tools/rominfo.py rom/golden_sun_fr.gba [autre.gba ...]
    python tools/rominfo.py --json rom/*.gba
"""

import argparse
import hashlib
import json
import sys
import zlib
from pathlib import Path

# Positions dans l'en-tête GBA (cartouche, à partir de 0x08000000 en mémoire)
HEADER_TITLE = slice(0xA0, 0xAC)      # 12 octets ASCII
HEADER_GAME_CODE = slice(0xAC, 0xB0)  # 4 octets : ex. "AGSF"
HEADER_MAKER = slice(0xB0, 0xB2)      # 2 octets : "01" = Nintendo
HEADER_FIXED = 0xB2                   # doit valoir 0x96
HEADER_VERSION = 0xBC
HEADER_CHECKSUM = 0xBD
HEADER_SIZE = 0xC0

# 3 premières lettres du code de jeu -> titre
GAMES = {
    "AGS": "Golden Sun",
    "AGF": "Golden Sun : L'Âge Perdu",
}

# Dernière lettre du code de jeu -> région
REGIONS = {
    "E": "USA",
    "P": "Europe (multilingue)",
    "F": "France",
    "D": "Allemagne",
    "S": "Espagne",
    "I": "Italie",
    "J": "Japon",
}


def header_checksum(data: bytes) -> int:
    """Complément calculé par le BIOS sur les octets 0xA0..0xBC."""
    return (-sum(data[0xA0:0xBD]) - 0x19) & 0xFF


def analyse(path: Path) -> dict:
    data = path.read_bytes()
    if len(data) < HEADER_SIZE:
        raise ValueError(f"{path} : fichier trop petit pour être une ROM GBA ({len(data)} octets)")

    code = data[HEADER_GAME_CODE].decode("ascii", errors="replace")
    expected = header_checksum(data)

    return {
        "fichier": str(path),
        "taille": len(data),
        "titre_interne": data[HEADER_TITLE].rstrip(b"\x00").decode("ascii", errors="replace"),
        "code_jeu": code,
        "jeu": GAMES.get(code[:3], "inconnu"),
        "region": REGIONS.get(code[3:], "inconnue"),
        "editeur": data[HEADER_MAKER].decode("ascii", errors="replace"),
        "version": data[HEADER_VERSION],
        "entete_valide": data[HEADER_FIXED] == 0x96 and data[HEADER_CHECKSUM] == expected,
        "crc32": f"{zlib.crc32(data):08x}",
        "md5": hashlib.md5(data).hexdigest(),
        "sha1": hashlib.sha1(data).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("roms", nargs="+", type=Path, help="fichiers .gba à analyser")
    parser.add_argument("--json", action="store_true", help="sortie JSON")
    args = parser.parse_args()

    results = []
    for rom in args.roms:
        try:
            results.append(analyse(rom))
        except (OSError, ValueError) as err:
            print(f"Erreur : {err}", file=sys.stderr)
            return 1

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    for info in results:
        print(f"== {info['fichier']}")
        print(f"  Jeu            : {info['jeu']} ({info['region']})")
        print(f"  Code / titre   : {info['code_jeu']} / {info['titre_interne']}")
        print(f"  Éditeur        : {info['editeur']}   version : {info['version']}")
        print(f"  Taille         : {info['taille'] // 1024 // 1024} Mo ({info['taille']} octets)")
        print(f"  En-tête valide : {'oui' if info['entete_valide'] else 'NON (dump corrompu ?)'}")
        print(f"  CRC32          : {info['crc32']}")
        print(f"  SHA-1          : {info['sha1']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
