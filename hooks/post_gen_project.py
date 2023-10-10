import re
import sys

PROJECT_REGEX = r"^[_a-zA.Z][-a-zA-Z0-9]+$"
project_name = "{{cookiecutter.project_name}}"

if not re.match(PROJECT_REGEX, project_name):
    raise ValueError("%s is not a valid Python project name")