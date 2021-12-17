# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in my_custom_maintenance/__init__.py
from my_custom_maintenance import __version__ as version

setup(
	name="my_custom_maintenance",
	version=version,
	description="Track status of workstations, schedule and manage corrective and preventive maintenance.",
	author="cjs",
	author_email="chiajunshen8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
