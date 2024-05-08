from setuptools import setup, find_packages

setup(
    name="python100",
    version="0.1.0",
    description="The collection of small programs written in Python as a part of the Python in 100 days course",
    author="Andriy Kandzyuba",
    author_email="andrey.kandzuba@gmail.com",
    url="https://github.com/andrewkandzuba/python100",
    packages=find_packages(),
    install_requires=[
        # add your project dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)