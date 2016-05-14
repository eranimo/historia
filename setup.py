from setuptools import setup, find_packages

setup(
    name = 'historia',
    packages = find_packages(),
    entry_points = {
        'console_scripts': ['historia = historia.historia:main']
    },
    author = 'Kaelan Cooter',
    author_email = 'me@kaelan.org'
)
