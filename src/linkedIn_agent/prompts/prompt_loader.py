from jinja2 import Environment, FileSystemLoader
import json

def prompt_loader(file, context, key):
    """
    Loads and renders a Jinja2 template, returning the requested JSON field.

    :param file: The Jinja2 template filename.
    :param context: A string that will be assigned to 'user_topic'.
    :param key: The key to extract from the JSON output.
    :return: The value corresponding to the key in the rendered JSON.
    """

    # Define the template directory
    template_dir = r"C:\Users\LENOVO\1. Projects\LinkedIn Agent\src\linkedIn_agent\prompts\prompt_templates"

    # Initialize the Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))

    # Load the template
    template = env.get_template(file)

    # Wrap the string inside a dictionary for Jinja2 to process correctly
    rendered = template.render(user_topic=context)

    # Parse the rendered template as JSON
    try:
        data = json.loads(rendered)
        return data[key]  # Return only the requested key
    except json.JSONDecodeError:
        raise ValueError(f"Template '{file}' did not render as valid JSON.")
    except KeyError:
        raise KeyError(f"Key '{key}' not found in the rendered template.")
