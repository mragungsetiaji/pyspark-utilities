import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyspark-utilities",
    version="0.0.1",
    author="Agung Setiaji",
    description="ETL focused utilities library for PySpark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mragungsetiaji/pyspark-utilities",
    packages=setuptools.find_packages(),
    install_requires=['numpy==1.14.5',
                      'pandas>=0.24.0',
                      'pyarrow==0.13.0',
                      'pyspark>=2.4.0'
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],
)