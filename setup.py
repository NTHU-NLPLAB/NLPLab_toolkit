import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

PYPI_NAME = "linggle"

with open(f"{PYPI_NAME}/requirements.txt") as fp:
    install_requires = fp.readlines()

install_requires = filter(lambda x: x.strip() != "", install_requires)
install_requires = list(install_requires)

setuptools.setup(
    name=PYPI_NAME,
    version="0.0.5",
    author="sappy5678, dspp779, ",
    author_email="sappy@nlplab.cc, jjc@nlplab.cc, isaackch@nlplab.cc",
    description="This toolkit contains APIs for Linggle, LinggleGEC, LinggleWrite, and LinggleBooster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NTHU-NLPLAB/NLPLab_toolkit",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
