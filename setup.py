import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "adityapandey258d"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "adityapandey258d@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_descriptiosn_content="text/markdown",
    url="https://github.com/adityapandey258d/" + REPO_NAME,
    package_urls={
        "Bug Tracker": "https://github.com/adityapandey258d/Text-Summarizer/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)