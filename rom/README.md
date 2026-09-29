# rom/

Placez ici **vos propres dumps** (jamais versionnés, voir `.gitignore`) :

- `golden_sun_us.gba` et `golden_sun_age_perdu_us.gba` : référence (code, cartes, stats, graphismes)
- `golden_sun_fr.gba` et `golden_sun_age_perdu_fr.gba` : texte, police, images avec du texte

Puis vérifiez-les :

```
python tools/rominfo.py rom/*.gba
```
