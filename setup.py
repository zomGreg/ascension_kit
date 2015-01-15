import os
from setuptools import setup

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['requests>=1.0.4', 'beautifulsoup4>=4.3.2']
setup(
    name = "Ascension Kit",
    version = "0.0.1",
    author = "Greg Moselle",
    author_email = "zomgreg+ascensionkit@gmail.com",
    description = ("A utility to report ascension information from NAO."),
    license = "BSD",
    keywords = "python nethack utility",
    url = "http://packages.python.org/ascension_kit",
    packages=['ascension_kit'],
    long_description=read('README'),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)