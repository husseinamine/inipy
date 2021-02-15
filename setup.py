import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ini.py",
    version="0.0.4",
    author="Hussein Raed",
    author_email="me@husseinraed.cf",
    description="a lightweight ini parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/husseinraed/ini.py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)