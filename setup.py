import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    license='GNU 3.0',
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.anthonyrolfe.rocks',
    author='Anthony Rolfe',
    author_email='anthony@anthonyrolfe.rocks',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.5',  # replace "2.5" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
