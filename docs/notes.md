# Notes de rétro-ingénierie

## ROM identifiées

| Jeu | Code | CRC32 | SHA-1 |
|---|---|---|---|
| Golden Sun (FR) | | | |
| L'Âge Perdu (FR) | | | |

## Rappels GBA

- CPU ARM7TDMI (code ARM 32 bits et Thumb 16 bits), 16,78 MHz
- ROM mappée à `0x08000000` : une adresse ROM `0x08XXXXXX` = offset fichier `0x0XXXXXX`
- Écran 240×160, tuiles 8×8 en 4 bpp (16 couleurs) ou 8 bpp (256 couleurs)
- Couleurs en BGR555 sur 16 bits : `0bbbbbgggggrrrrr`

## Sources communautaires

À compléter au fil de l'eau (lien, ce qui a été vérifié, adresse US ↔ adresse FR).

## Formats

À compléter : compression, texte, cartes, données de jeu.
