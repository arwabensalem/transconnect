# AI_LOG — Workshop Models TransConnect (Part 1)

## Entrée [2026-10-06] — Bug Hunt Offre

- **Outil IA utilisé :** Cursor (Composer)
- **Prompt :** Analyse du jet IA de `Offre` fourni dans le workshop ; identification et correction des 4 anomalies ; alignement de tous les modèles sur le cahier des charges ; rédaction de ce log.
- **Sortie obtenue (résumé) :** Code `Offre` initialement recopié du jet buggy ; audit croisé avec le PDF (contraintes de modélisation + Bug Hunt) ; corrections appliquées sur les 5 entités.
- **Écarts identifiés vs cahier des charges :**
  1. `prix` déclaré en `CharField` alors que le cahier impose un `DecimalField` (montant monétaire).
  2. `delai_jours` déclaré en `IntegerField` (accepte les négatifs) alors que le cahier impose un `PositiveIntegerField`.
  3. `date_proposition` avec `auto_now=True` (se met à jour à chaque `save`) alors que le cahier impose `auto_now_add=True` (date figée à la création).
  4. `vehicule` avec `null=True` alors qu'une offre doit être associée à un véhicule disponible ; absence aussi de `created_at` / `updated_at` (obligatoires sur tous les modèles).
- **Correction apportée et justification :**
  1. `prix = DecimalField(max_digits=10, decimal_places=2)` — type adapté aux montants, conforme au tableau de contraintes.
  2. `delai_jours = PositiveIntegerField()` — interdit les délais négatifs.
  3. `date_proposition = DateField(auto_now_add=True)` — conserve la date de proposition d'origine.
  4. `vehicule` sans `null=True` (FK obligatoire) + ajout de `created_at` / `updated_at` ; suppression du `save()` vide inutile.
  - Autres écarts corrigés hors Bug Hunt : `matricule_fiscal` max_length=17, champ `utilisateur` (ex-`gerant`), statuts `Expedition` (`attribuee` / `annulee`, suppression de la valeur erronée `chargeur`), génération auto de `user_id` (UserManager) et de `reference`, `capacite_kg` en `PositiveIntegerField`.

## Entrée [2026-10-06] — Alignement global models.py

- **Outil IA utilisé :** Cursor (Composer)
- **Prompt :** Appliquer toutes les corrections listées dans l'audit du workshop (Utilisateur, Entreprise, Vehicule, Expedition, Offre) et régénérer les migrations.
- **Sortie obtenue (résumé) :** `models.py` des 4 apps réécrits ; `AI_LOG.md` créé ; migrations `0001_initial` régénérées et appliquées sur `Arwa.sqlite3`.
- **Écarts identifiés vs cahier des charges :** voir entrée Bug Hunt + checklist section VIII du PDF.
- **Correction apportée et justification :** modèles alignés sur le diagramme de classe et le tableau de contraintes ; base nommée `Arwa.sqlite3` déjà conforme.
