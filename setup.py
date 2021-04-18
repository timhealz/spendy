import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spendy-timhealz",
    version="1.0.1",
    author="Tim Healy",
    author_email="healyt22@gmail.com",
    description="Package for processing financial data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timhealz/spendy",
    project_urls={
        "Issues": "https://github.com/timhealz/spendy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "SQLAlchemy",
        "PyMySQL",
    ]
)
