from jinja2 import Environment, FileSystemLoader
import json
from pathlib import Path

class TemplateManager:
    def __init__(self, template_folder: str):
        self.env = Environment(loader=FileSystemLoader(template_folder))
        self.template_folder = template_folder
    def load_template(self, template_name: str):
        return self.env.get_template(template_name)
    def render_prompt(self, template_name: str, **kwargs):
        # print(f"Rendering template '{template_name}' with variables: {kwargs}")
        template = self.load_template(template_name)
        return template.render(**kwargs)
    
    def get_template_content(self, template_name: str):
        template_path = Path(self.template_folder) / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template file '{template_name}' not found in '{self.template_folder}'.")
        return template_path.read_text()
 
 