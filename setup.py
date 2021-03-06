import os
from setuptools import setup

requires = (
        "requests>=0.13.6",
        "python-dateutil>=1.5",
        "beautifulsoup4",
        "requests",
        "mysql-connector-python",
        "wikitools",
        "mwlib",
        "mwparserfromhell",
        "flask",
        "gunicorn"
        )

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bigfootgenes",
    version = "0.0.1",
    author = "Tomster and Ginster",
    author_email = "sudogenes",
    description = ("useless"),
    license = "PRIVATE",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['package_name',],
    # namespace_packages = ['package_name'],
    install_requires=requires,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: PRIVATE",
    ],
)
