from setuptools import setup, find_packages


setup(
	name='aioscrape',
	version='0.0.1',
	author='sayori',
	description='Scrape multiple urls asynchronously',
	packages=find_packages(exclude=('tests',)),
	install_requires=[]
)