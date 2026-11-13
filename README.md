# capstone-devops-NOMEQUIPE

API FastAPI du fil rouge du cours DevOps et IA (ESISA, 2026-2027).
Ce dépôt contient l'API, ses tests, la CI GitHub Actions et l'environnement reproductible.

## Structure

| Dossier | Contenu |
|---|---|
| `app/` | API FastAPI (`/health`, `/ready`, `/predict`, `/error`, `/metrics`) |
| `tests/` | Tests pytest |
| `agent/` | Agent du fil rouge |
| `infra/` | Fichiers d'infrastructure |
| `.devcontainer/` | Configuration Codespaces |
| `.github/` | Workflows CI |

Rôles de l'équipe et Definition of Done : voir [ROLES.md](ROLES.md).

## Prérequis

- Compte GitHub
- Git
- Python 3.12 (ou un Codespace, ou Docker)

## Option A : GitHub Codespaces (recommandé)

1. Sur GitHub : **Code, Codespaces, Create codespace on main**.
2. Vérifier l'environnement :
```bash
   python --version
   git --version
```
3. Passer à la section « Installation ».
4. **Arrêter le Codespace après usage** (quota gratuit limité) :
   github.com/codespaces, puis `...`, puis **Stop codespace**.

## Option B : en local

```bash
git clone https://github.com/aissatabarry2/capstone-starter.git
cd capstone-starter
```

## Installation

Linux, macOS ou Codespaces :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

Windows (PowerShell) :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt -r requirements-dev.txt
```

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

Vérifier que l'API répond :

```bash
curl -s localhost:8000/health
```

Réponse attendue : `{"status":"ok"}`.

La page `/` renvoie 404 : c'est normal, aucune route n'est définie à la racine.
La documentation interactive est disponible sur `/docs`.

## Lint et tests

```bash
ruff check .
pytest
```

Les deux commandes doivent passer. La CI (GitHub Actions) les exécute à chaque push.

## Règles du dépôt

- Un seul dépôt pour toute l'équipe.
- Ne jamais committer de fichier `.env`, de jeton ou de clé d'API (`.env` et `.venv/` sont dans `.gitignore`).
- Une carte Notion = une branche = une pull request.
- Messages de commit clairs (`feat:`, `fix:`, `docs:`, `chore:`).
- L'IA propose, l'humain valide : lint et tests avant tout commit.

## Intégration continue (CI)

Le workflow GitHub Actions `.github/workflows/ci.yml` s'exécute à chaque pull request et à chaque push sur `main`.

| Étape | Rôle |
|---|---|
| `actions/checkout` | Récupère le code |
| `actions/setup-python` (Python 3.12, `cache: pip`) | Installe Python et met en cache les dépendances |
| `pip install -r requirements.txt -r requirements-dev.txt` | Installe les dépendances |
| `ruff check .` | Lint |
| `pytest -q --junitxml=report.xml` | Tests, avec un rapport XML |
| `actions/upload-artifact` (`if: always()`) | Sauvegarde `report.xml` comme artefact `test-report`, même si les tests échouent |

Le job s'appelle `test`. C'est un check **obligatoire** : le ruleset de `main` refuse la fusion d'une PR tant qu'il n'est pas vert.

### Lancer les mêmes vérifications en local

```bash
ruff check .
pytest -q
```

### Lire un échec de la CI

1. Ouvrir la PR, puis **Details** à côté de `ci / test` (ou l'onglet **Actions**).
2. Repérer l'étape marquée d'une croix rouge et déplier son log.
3. Pour un échec de test, lire la ligne `FAILED ...` et la comparaison `assert valeur_reçue == valeur_attendue`.
4. Télécharger l'artefact `test-report` (section **Artifacts** du résumé du run) pour consulter `report.xml`.

### Mesure du cache pip

Durées totales relevées dans l'onglet Actions :

| Situation | Durée du run |
|---|---|
| Sans cache (runs avant la modification) | 15 s à 19 s |
| Avec `cache: pip` (premier run, création du cache) | 15 s |
| Avec `cache: pip` (runs suivants) | 18 s et 23 s |

Aucun gain mesurable : le projet n'a que peu de dépendances légères, donc l'installation est déjà rapide, et la durée varie de quelques secondes d'un run à l'autre selon la machine. Le cache devient utile avec des dépendances lourdes.

### Exemple de cycle rouge puis vert

Un test a été volontairement cassé (`test_health` attendait `"ko"` au lieu de `"ok"`) : la CI est passée au rouge à l'étape `Run pytest`. Le test a ensuite été corrigé et la CI est repassée au vert.