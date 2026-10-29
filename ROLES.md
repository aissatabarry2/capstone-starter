# Rôles et Definition of Done

Projet : capstone-devops-NOMEQUIPE
Semaine : S1 (culture DevOps)

## Rôles de l'équipe

| Rôle | Responsable | Mission principale |
|---|---|---|
| Product Owner / Scrum Master | Aissata | Tient le backlog Notion à jour, fixe les priorités, anime le point d'équipe, la revue et la rétrospective de sprint |
| Développeur backend | Fatoumata | Développe et maintient l'API FastAPI (routes, logique métier, tests unitaires) |
| Ingénieur DevOps / CI-CD | Barry | Gère le dépôt, la CI GitHub Actions, l'environnement reproductible (Codespaces / Docker) et la gestion des secrets |
| Qualité et documentation | Sall | Relit les pull requests, vérifie les tests et le lint, tient à jour le README et la documentation |

## Definition of Done

Une carte ne passe à « Terminé » que si **tous** les points suivants sont validés :

- [ ] Les tests sont verts (`pytest`) et le lint passe (`ruff check .`)
- [ ] La CI GitHub Actions est verte sur la branche concernée
- [ ] Une revue de code a été faite par un autre membre de l'équipe
- [ ] La documentation (README, ROLES.md) est à jour
- [ ] Aucun secret (`.env`, jeton, clé d'API) n'est présent dans le dépôt
- [ ] La carte Notion est mise à jour (statut, lien vers la PR, date de fin)

## Règles de travail

- Un seul dépôt pour toute l'équipe.
- Une carte Notion = une branche = une pull request.
- Aucun commit direct sur `main` sans que les tests passent.
- L'IA propose, l'humain valide : tout code généré est relu, avec lint et tests lancés.