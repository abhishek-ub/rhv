
from setuptools import setup, find_packages
from rhv.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='rhv',
    version=VERSION,
    description='view RH in terminal',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='aks',
    author_email='mailaks.ism@gmail.com',
    url='https://github.com/abhishek-ub/rhv',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'rhv': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        rhv = rhv.main:main
    """,
)
