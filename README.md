# Flask Cookiecutter Template

This is a Cookiecutter template for creating Flask web applications. It provides a basic project structure and configuration to help you get started quickly with Flask development.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed.
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html) installed. You can install it using pip: `pip install cookiecutter`.

## Usage

To create a new Flask project using this template, follow these steps:

1. Open your terminal and navigate to the directory where you want to create your Flask project.

2. Run the following command, replacing `<template-repo>` with the URL of this Cookiecutter template:

   ```bash
   cookiecutter <template-repo>
   ```

   For example:

   ```bash
   cookiecutter https://github.com/DominikBalga/flask-cookiecutter-template
   ```

3. You will be prompted to provide values for template variables such as `project_name`, `author_name`, and other project-specific settings.

4. Once you've provided the values, Cookiecutter will generate a new Flask project folder with the structure defined in this template.

5. Navigate to the newly created project directory:

   ```bash
   cd your-flask-project
   ```

6. Install Poetry: Ensure that you have Poetry installed on your system. If not, you can install it using pip:

   ```bash
   pip install poetry
   ```

7. Create and activate a virtual environment for your project (recommended) + install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   pip install poetry
   ```

8. Customize the Flask application inside the project directory according to your requirements. You can define routes, templates, and add functionality as needed.

9. To run your Flask application locally, use the following command:

   ```bash
   python app.py
   ```

   Your application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

Here is a brief overview of the project structure:

- `app/`: Contains the core of your Flask application, including routes, models, views, forms, templates, and static files.
- `tests/`: Directory for unit tests.
- `.gitignore`: Specifies files and directories to ignore in version control.
- `app.py`: Entry point to run your Flask application.
- `README.md`: Documentation for your template.

Please feel free to customize this template to better suit your project's needs.

## License

This template is released under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.


_______________________________

- [ ] TODO config.py??
