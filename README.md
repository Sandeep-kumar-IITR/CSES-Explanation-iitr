# CSES Problem Explanations

A Django-based web application for organizing and presenting explanations for problems from the CSES Problem Set.

## Repository layout

The project contains Django application modules, templates and static assets:

- `manage.py` — Django management entry point.
- `CSESExplanation/` and `main/` — project/application code.
- `topic/` — topic-oriented content.
- `templates/` and `static/` — presentation assets.
- `requirements.txt` — Python dependencies.

## Local setup

```bash
git clone https://github.com/Sandeep-kumar-IITR/CSES-Explanation-iitr.git
cd CSES-Explanation-iitr
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the local address printed by Django.

## Notes

The repository currently includes a SQLite database file. Before sharing a public deployment or accepting contributions, replace any personal or non-public records with synthetic seed data and keep local database files out of version control.

## Author

Sandeep Kumar · [GitHub](https://github.com/Sandeep-kumar-IITR)
