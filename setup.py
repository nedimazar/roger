from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="roger-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["roger=src.roger.roger:main"]},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
