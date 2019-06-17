import os
import sys
import platform
import configparser
from setuptools import setup


if sys.version_info[0] < 3:
    raise Exception(
    )

config = configparser.ConfigParser()

current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'setup.cfg')

config.read(config_file_path)

VERSION = config['chatterbot']['version']
AUTHOR = config['chatterbot']['author']
AUTHOR_EMAIL = config['chatterbot']['email']
URL = config['chatterbot']['url']

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

REQUIREMENTS = []
DEPENDENCIES = []

with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
        if requirement.startswith('git+git://'):
            DEPENDENCIES.append(requirement)
        else:
            REQUIREMENTS.append(requirement)


setup(
    name='ChatterBot',
    version=VERSION,
    url=URL,
    download_url='{}/tarball/{}'.format(URL, VERSION),
    project_urls={
    },
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    test_suite='tests'
)
