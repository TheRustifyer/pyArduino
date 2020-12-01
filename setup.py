import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyArduino", # Replace with your own username
    version="0.1.0",
    author="Alex Vergara",
    author_email="pyryzyab@tutanota.com",
    description="Python module to handle Arduino comunication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
          'pyserial',
          'pyfirmata'
      ],
    url="https://github.com/Pyryzyab/pyArduino",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
