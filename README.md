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