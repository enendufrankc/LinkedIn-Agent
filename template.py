import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

TEMPLATES = [
    {
        "name": "linkedIn_agent",
        "files": [
            "src/linkedIn_agent/__init__.py",
            "src/linkedIn_agent/tools/__init__.py",
            "src/linkedIn_agent/tools/linkedIn_scraper.py",
            "src/linkedIn_agent/tools/linkedIn_influencer.py",
            "src/linkedIn_agent/tools/linkedIn_post_creator.py",
            "src/linkedIn_agent/tools/run_tools.py",
            "src/linkedIn_agent/clients/__init__.py",
            "src/linkedIn_agent/clients/llm.py",
            "src/linkedIn_agent/agents/__init__.py",
            "src/linkedIn_agent/agents/scraper_agent.py",
            "src/linkedIn_agent/agents/websearcher_agent.py",
            "src/linkedIn_agent/agents/post_creator_agent.py",
            "src/linkedIn_agent/agents/influencer_agent.py",
            "src/linkedIn_agent/utils/__init__.py",
            "src/linkedIn_agent/utils/common.py",
            "src/linkedIn_agent/config/__init__.py",
            "src/linkedIn_agent/config/configuration.py",
            "src/linkedIn_agent/test/__init__.py",
            "src/linkedIn_agent/entity/__init__.py",
            "src/linkedIn_agent/entity/config_entity.py",
            "src/linkedIn_agent/constants/__init__.py",
            "src/linkedIn_agent/tasks/tasks.py",
        ],
    },
]

PROJECT_FILES = [
    "README.md",
    "LICENSE",
    ".gitignore",
    "pyproject.toml",
    "setup.py",
    "tests/test_cli.py",
    ".env.example",
    ".github/workflows/ci.yml",
    "main.py",
    "requirements.txt",
    "README.md",
    "config/config.yaml",
    "config/config-dev.yaml",
    "config/config-prod.yaml",
    "Dockerfile",
    "docker-compose.yml",
    "params.yaml",
    "schema.yaml",
    ".streamlit/config.toml",
    ".streamlit/secrets.toml",
    "app.py",
    "research/trials_01.ipynb",
]

def create_file(file_path):
    full_path = Path(file_path)
    if full_path.parent:
        os.makedirs(full_path.parent, exist_ok=True)
    if not full_path.exists():
        with open(full_path, "w", encoding="utf-8") as f:
            pass
        logging.info(f"Created file: {full_path}")

def create_files(template_list, project_files):
    for file_path in project_files:
        create_file(file_path)

    for template in template_list:
        template_dir = Path(template['name'])
        for file_path in template["files"]:
            create_file(template_dir / file_path)

if __name__ == "__main__":
    create_files(TEMPLATES, PROJECT_FILES)