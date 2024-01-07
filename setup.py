from setuptools import setup, find_packages

setup(
    name="swiftdeploy",
    version="0.5.1",
    author="Akinrotimi Daniel F",
    author_email="dtenny95@gmail.com",
    description="This package provides a web application wrapper for your machine learning models.",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/firebreather-heart/swiftdeploy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Flask',
    ],
)