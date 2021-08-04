import setuptools
import os
import io

def read(file_name):

    """Read a text file and return the content as a string."""
    try:
        with io.open(
            os.path.join(os.path.dirname(__file__), file_name), encoding="utf-8"
        ) as f:
            return f.read()
    except:
        return ""
        
setuptools.setup(
    name="fiftyone_pipeline_engines_fiftyone",
    version=read("version.txt"),
    author="51Degrees",
    author_email="support@51degrees.com",
    url="https://51degrees.com/",
    description=("The 51Degrees Pipeline API is a generic web request intelligence and data processing solution with the ability to add a range of 51Degrees and/or custom plug ins (Engines). "
    "It includes a ShareUsage engine that sends usage data to 51Degrees in zipped batches."),
    long_description=read("readme.md"),
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    install_requires=[
          'fiftyone_pipeline_engines',
          'requests',
          'cachetools'
    ],
    packages=["fiftyone_pipeline_engines_fiftyone"],
    license="EUPL-1.2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    include_package_data=True
)
