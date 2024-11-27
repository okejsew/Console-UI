from setuptools import setup

setup(
    name='Console-UI',
    version='1.1.2',
    url='https://github.com/okejsew/Console-UI',
    install_requires=[
        'windows-curses; platform_system=="Windows"',
    ],
)