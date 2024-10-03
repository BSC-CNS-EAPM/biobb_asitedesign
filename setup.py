import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_asitedesign",
    version="1.2",
    author="Biobb developers",
    author_email="albert.canella@bsc.es",
    description="AsiteDesign repository combines the PyRosetta modules with enhanced sampling techniques to design "
                "both the catalytic and non-catalytic residues in given active sites.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_asitedesign",
    project_urls={
        "Documentation": "http://biobb_ahatool.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['adapters', 'docs', 'test']),
    package_data={'biobb_asitedesign': ['py.typed']},
    install_requires=['biobb_common==4.0.0'],
    python_requires='>=3.7,<3.10',
    entry_points={
        "console_scripts": [
            "asitedesign = biobb_asitedesign.asitedesign.asitedesign:main"
        ]
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
