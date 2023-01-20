import os
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    "pytest",
    "troposphere>=2.3.2",
    "schematics>=2.1.1",
    "stacker @ git+https://github.com/remind101/stacker-internal.git",
]

tests_require = [
    "cfn_flip (==1.0.2)",
    "mock (==2.0.0)",
    "schematics (==2.2.1)",
    "stacker (>=1.4.0)",
]


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == "__main__":
    setup(
        name="stacker_blueprints",
        version="1.0.8",
        author="Michael Barrett",
        author_email="loki77@gmail.com",
        license="New BSD license",
        url="https://github.com/remind101/stacker_blueprints",
        description="Default blueprints for stacker",
        long_description=read("README.rst"),
        packages=find_packages(),
        install_requires=install_requires,
        # dependency_links=[
        #     'https://github.com/Lowercases/stacker/archive/refs/tags/python3.tar.gz#egg=stacker-python3',
        # ],
        requires=tests_require,
    )
