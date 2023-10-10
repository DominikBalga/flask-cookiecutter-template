import re
import sys
import os
import urllib.request

PROJECT_REGEX = r"^[_a-zA.Z][-a-zA-Z0-9]+$"

def download_image(image_url, destination_folder):
    try:
        image_name = os.path.basename(image_url)
        destination_path = os.path.join(destination_folder, image_name)
        urllib.request.urlretrieve(image_url, destination_path)
        print(f"Downloaded {image_name} to {destination_path}")
    except Exception as e:
        print(f"Error downloading image: {str(e)}")


if __name__ == "__main__":
    project_name = "{{cookiecutter.project_name}}"
    if not re.match(PROJECT_REGEX, project_name):
        print("%s is not a valid Python project name" %project_name)
        sys.exit(1)
    logo_img_url = "{{cookiecutter.logo_img_url}}"
    static_folder = "{{cookiecutter.project_name}}/static/images"
    if logo_img_url.lower() == "n" or logo_img_url.lower() == "no":
        download_image(logo_img_url, static_folder)