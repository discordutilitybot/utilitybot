import setuptools
from setuptools import setup

readme = ''
with open('README.md') as f:
    readme = f.read()


setup(name='utilitybot',
    author='Andrew Nijmeh',
    url="https://discordutilitybot/utilitybot",
    version='development',
    packages=['command, cog, events, plugins, tests, utils, assets'],
    license='MIT',
    description='A open-source mutli-purpose discord bot with integration, music, moderation and alot more!',
    long_description=readme,
    include_package_data=False,
    install_requires='requirements.txt',
    python_requires='>=3.5.2',

)