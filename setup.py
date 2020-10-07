import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nba-kevin-bacon-TScafeJR", # Replace with your own username
    version="0.0.1",
    author="Tyrone Scafe",
    author_email="tscafejr@gmail.com",
    description="This is a network graph of nba teammates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TScafeJR/nba-kevin-bacon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)