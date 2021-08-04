#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess
import os


def write_version_file(version):
    """Writes a file with version information to be used at run time
    Parameters
    ----------
    version: str
        A string containing the current version information
    Returns
    -------
    version_file: str
        A path to the version file
    """
    try:
        git_log = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%h %ai"]
        ).decode("utf-8")
        git_diff = (
            subprocess.check_output(["git", "diff", "."])
            + subprocess.check_output(["git", "diff", "--cached", "."])
        ).decode("utf-8")
        if git_diff == "":
            git_status = "(CLEAN) " + git_log
        else:
            git_status = "(UNCLEAN) " + git_log
    except Exception as e:
        print(f"Unable to obtain git version information, exception: {e}")
        git_status = ""

    version_file = ".version"
    if os.path.isfile(version_file) is False:
        with open("rmnest/" + version_file, "w+") as f:
            f.write(f"{version}: {git_status}")

    return version_file


def get_long_description():
    """ Finds the README and reads in the description """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "README.md")) as f:
        long_description = f.read()
    return long_description


# get version info from __init__.py
def readfile(filename):
    with open(filename) as fp:
        filecontents = fp.read()
    return filecontents


VERSION = "0.1.2"
version_file = write_version_file(VERSION)
long_description = get_long_description()

setup(
    name="rmnest",
    description="Faraday rotation measurement for pulsars and FRBs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlower/rmnest",
    author="Marcus Lower",
    author_email="mlower@swin.edu.au",
    license="MIT",
    version=VERSION,
    packages=find_packages(exclude=["test", "venv", "priors"]),
    package_dir={"rmnest": "rmnest"},
    package_data={"rmnest": [version_file]},
    install_requires=["future", "numpy", "scipy", "matplotlib", "bilby"],
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': ['rmnest=rmnest.fit_RM:main'],
    }
)
