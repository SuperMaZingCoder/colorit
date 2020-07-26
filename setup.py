import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color-it",
    version="1.1.1",
    author="SuperMaZingCoder",
    author_email="supermazingcoder@gmail.com",
    description="A cross-platform lightweight package for printing colors in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeForeverAndEver/colorit",
    packages=["colorit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["colorama"],
    include_package_data=True
)