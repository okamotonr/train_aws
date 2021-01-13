"""sample setup.py of sample_pkg"""
from setuptools import find_packages, setup

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements


REQUIRES = parse_requirements('./requirements.txt', session=None)

setup(
    name="sample_pkg",
    use_scm_version=True,
    packages=find_packages(exclude=['tests']),
    requires=REQUIRES,
    setup_requires=['setuptools_scm'],
)
