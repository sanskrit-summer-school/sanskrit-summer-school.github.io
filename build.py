import yaml
from jinja2 import Environment, FileSystemLoader
import os

def load_yaml(filename):
    with open(f"data/{filename}", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_site():
    print("Loading YAML data...")
    
    # Load all data sections
    data_context = {
        "hero": load_yaml("hero.yml"),
        "overview": load_yaml("overview.yml"),
        "objectives": load_yaml("objectives.yml"),
        "audience": load_yaml("audience.yml"),
        "schedule": load_yaml("schedule.yml"),
        "speakers": load_yaml("speakers.yml")
    }

    print("Rendering template...")
    # Setup Jinja2 environment looking in the current directory
    env = Environment(loader=FileSystemLoader(searchpath="."))
    template = env.get_template("template.html")

    # Render the HTML with our data
    output_html = template.render(data_context)

    # Save to index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output_html)

    print("✅ Build complete! Open index.html in your browser.")

if __name__ == "__main__":
    build_site()