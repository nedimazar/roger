from setuptools import setup, find_packages

# Handling the requirements file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Handling the README file for long description
with open("README.md") as f:
    long_description = f.read()

setup(
    name="roger-cli",
    version="0.2.0",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["roger=roger.roger:main"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
)
