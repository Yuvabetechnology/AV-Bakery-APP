from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in av_bakery/__init__.py
from av_bakery import __version__ as version

setup(
	name="av_bakery",
	version=version,
	description="Order Management ",
	author="mariya@yuvabe.com",
	author_email="mariya@yuvabe.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
