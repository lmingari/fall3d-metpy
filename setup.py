import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metpy-lmingari", 
    version="1.0",
    author="Leonardo Mingari",
    author_email="leonardo.mingari@bsc.es",
    description="Met utilities for the FALL3D model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmingari/metpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
