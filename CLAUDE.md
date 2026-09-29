# Contexte du projet

Remake d'étude **privé** de *Golden Sun* et *Golden Sun : L'Âge Perdu* (GBA), dans Unity.
Répondre en **français**.

## Décisions prises

- **Moteur : Unity 6 LTS, URP (3D)**, visée graphique « HD-2D » (sprites dans un décor 3D,
  lumières, post-process). Unity choisi plutôt qu'Unreal pour que tout reste en texte
  (C#, YAML avec *Asset Serialization = Force Text*) et donc lisible/modifiable par Claude.
- **L'utilisateur connaît le C++ mais pas le C#** : expliquer au fil du code les différences
  (références vs pointeurs, struct vs class, GC, propriétés, LINQ…).
- **Outils de rétro-ingénierie en Python** dans `tools/`, sortie JSON/PNG dans `extracted/`,
  importée automatiquement dans Unity. Le moteur ne lit jamais la ROM directement.
- **ROM US = référence** (code, cartes, stats, scripts, graphismes) : la doc communautaire
  (Golden Sun Hacking Community, Golden Sun Editor d'Atrius) utilise les adresses US.
- **ROM FR = texte** : dialogues, noms (Psynergies, Djinns, objets, classes, ennemis), menus,
  police avec accents, images contenant du texte. Retrouver les tables FR par comparaison avec l'US.
- On commence par Golden Sun 1 ; L'Âge Perdu partage en grande partie le même moteur.

## Règles

- **Ne jamais versionner** de ROM, sauvegarde ou donnée extraite (voir `.gitignore`).
- Ne jamais inventer d'adresses ou de formats : vérifier dans la ROM (mGBA, Ghidra) ou citer la
  source communautaire, et consigner les résultats dans `docs/notes.md` (adresses US ↔ FR).
- Vérifier les dumps avec `python tools/rominfo.py rom/*.gba` et comparer le SHA-1 à No-Intro.
- Dépôt hébergé sur le GitLab personnel de l'utilisateur (Git LFS activé).

## Avancement

Voir la feuille de route dans `README.md`. Étape suivante : palettes et tuiles (étape 2).
