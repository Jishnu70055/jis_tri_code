from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in csa_new/__init__.py
from csa_new import __version__ as version

setup(
	name='csa_new',
	version=version,
	description='something',
	author='sd',
	author_email='a',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
