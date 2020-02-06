import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NTHU_NLPLab_toolkit", # Replace with your own username
    version="0.0.3",
    author="sappy5678",
    author_email="sappy@nlplab.cc",
    description="This toolkit is maintained by NTHU NLP Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NTHU-NLPLAB/NLPLab_toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)