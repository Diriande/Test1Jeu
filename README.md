# Test1Jeu — remake d'étude de Golden Sun (Unity)

Projet **privé et personnel**, à but d'apprentissage : rétro-ingénierie de *Golden Sun* et
*Golden Sun : L'Âge Perdu* (versions FR) et réimplémentation dans Unity avec un rendu modernisé.

> ⚠️ Aucune ROM ni donnée extraite n'est versionnée. Chacun fournit son propre dump dans `rom/`.

## Organisation

```
rom/        vos dumps .gba (ignorés par Git)
tools/      outils Python : identification, extraction, décompression
extracted/  sortie des outils : JSON, PNG (ignorée par Git)
docs/       notes de rétro-ingénierie (formats, adresses FR, sources communautaires)
unity/      projet Unity (URP)
```

Principe : **ROM → `tools/` → `extracted/` (JSON/PNG) → import automatique dans Unity**.
Le moteur ne lit jamais la ROM directement.

## Prérequis

- Python 3.10+
- Unity 6 LTS (URP), avec *Project Settings > Editor > Asset Serialization = Force Text*
- Git LFS (activé aussi côté GitLab) : `git lfs install`
- mGBA (débogueur) et Ghidra pour l'analyse

## Feuille de route

1. [ ] Identifier les ROM : `python tools/rominfo.py rom/*.gba`
2. [ ] Palettes et tuiles (format graphique GBA standard) → PNG
3. [ ] Décompression des formats propres à Golden Sun
4. [ ] Texte FR → JSON
5. [ ] Données de jeu : personnages, classes, Djinns, Psynergies, objets, ennemis → JSON
6. [ ] Cartes → JSON + visualiseur
7. [ ] Unity : déplacement sur grille avec placeholder
8. [ ] Unity : import automatique des JSON (ScriptableObjects)
9. [ ] Unity : Psynergie sur le décor (Déplacer, Croissance…) et énigmes
10. [ ] Unity : combats, Djinns, invocations
11. [ ] Direction artistique « HD-2D » : sprites dans un décor 3D, lumières, post-process

On commence par Golden Sun ; L'Âge Perdu partage en grande partie le même moteur.

## Note sur les adresses

La documentation communautaire donne en général les positions (offsets) de la **version US**.
Les versions FR sont décalées : on retrouve les données par motifs/signatures et on consigne
les adresses FR dans `docs/`.
