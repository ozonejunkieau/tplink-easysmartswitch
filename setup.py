import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tplink_easysmartswitch", # Replace with your own username
    version="0.0.1",
    author="Tristan Steele",
    author_email="tristan.steele@gmail.com",
    description="A library for tp-link Easy Smart Switches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ozonejunkieau/tplink-easysmartswitch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)