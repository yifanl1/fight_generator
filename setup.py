from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fight_generator',
    version='0.1.0',
    description='Simple tool to generate text simulations of custom fights',
    long_description=readme,
    author='Yifan Lu',
    author_email='yi.fan.lu2@gmail.com',
    url='https://github.com/yifanl1/fight_generator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
