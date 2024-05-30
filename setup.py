from setuptools import find_packages, setup

setup(
    name="harvest_cli",
    author="Bill Poulson",
    version="0.1",
    packages=find_packages(),
    py_modules=["cli", "authorization", "config", "harvest_client", "util"],
    install_requires=[
        "requests==2.26.0",
        "click>=8.0.1",
        "inquirer==3.1.4",
        "flask==3.0.3",
    ],
    entry_points={
        "console_scripts": [
            "harvest=cli:cli",  # Adjusted to point to the correct module
        ],
    },
)
