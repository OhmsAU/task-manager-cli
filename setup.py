from setuptools import setup, find_packages
nsetup(
    name="task-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "rich>=13.0"
    ],
    entry_points={
        "console_scripts": [
            "task-manager=src.cli:cli,
        ]
    },
)
