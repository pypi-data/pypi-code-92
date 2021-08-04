import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkt-Toolkit",
    version="1.7",
    author="Suprime",
    license = 'MIT',
    author_email="suprime.sendings@gmail.com",
    description="Useful collection of python packages and scripts.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MOBSkuchen/tkt-Toolkit",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx',
        'youtube-search-python',
        'cryptography',
        'pytube',
        'gtts',
        'discord',
        'googletrans==3.1.0a0',
        'SpeechRecognition',
        'termcolor',
        'playsound',
        'mediapipe',
        'opencv-python',
        'keyboard',
        'tesseract-ocr-data',
        'pytesseract'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)