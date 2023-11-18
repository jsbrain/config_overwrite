from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in config_overwrite/__init__.py
from config_overwrite import __version__ as version

setup(
	name="config_overwrite",
	version=version,
	description="App to overwrite various settings of ERPNext.",
	author="BradBit GmbH",
	author_email="manuel.maute@bradbit.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)