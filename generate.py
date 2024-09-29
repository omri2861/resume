import yaml
from jinja2 import Environment, FileSystemLoader


def main():
    with open("attempt.yaml", encoding='utf-8') as data_file:
        resume_data = yaml.safe_load(data_file)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    result = template.render(resume_data)

    with open("index.html", 'w', encoding='utf-8') as dest:
        dest.write(result)


if __name__ == "__main__":
    main()
