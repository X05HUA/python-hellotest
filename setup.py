import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloworld/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "hellotest",        # what you want to call the archive/egg
    version = version,
    packages=["hellotest"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {"hellotest": ["VERSION.txt"]},
    author="Testing Pacman",
    author_email = "testingpacman@gmail.com",
    description = "The familiar example program in Python",
    license = "Apache 2.0",
    keywords= "example documentation tutorial",
    url = "https://github.com/X05HUA/python-hellotest",
    
)
