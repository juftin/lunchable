import configparser

from lunchmoney.config import FileConfig

config_file = FileConfig.PROJECT_DIR.joinpath("setup.cfg")
requirements_file = FileConfig.PROJECT_DIR.joinpath("requirements.txt")

config = configparser.ConfigParser()
config.read(config_file)
packages = config["options"]["install_requires"].strip()

with open(requirements_file, "w", encoding="utf-8") as requirements_body:
    requirements_body.write(packages + "\n")
    requirements_body.seek(0)
