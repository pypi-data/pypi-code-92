from setuptools import find_packages, setup

import versioneer

setup(
    name="gosu",
    description="the extensible taskrunner",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "plumbum",
        "typer",
        "python-dotenv",
        "semver",
        "pytest",
        "pyupgrade",
        "isort",
        "black",
        "flake8",
        "mccabe",
        "flake8-comprehensions",
        "flake8-print",
        "flake8-cognitive-complexity",
        "pytest-xdist",
        "pytest-sugar",
        "coverage",
        "django_coverage_plugin",
        "pyupgrade",
        "twine",
    ],
    license_files=("LICENSE",),
    url="https://gitlab.com/tuhls/gosu",
    author="Herbert Rusznak (tlb)",
    author_email="herbert.rusznak@gmail.com",
    license="MIT",
    entry_points={"console_scripts": ("gosu = gosu.main:app",)},
)
