import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HTTPStatusCodes",
    version="1.0.1",
    author="iAmCharlottey",
    description="Returns a string detailing of what a given status code means.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CharlotteCross1998/HTTPStatusCodes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
    ],
)