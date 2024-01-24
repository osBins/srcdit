#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='srcdit',
    version='0.1.10',
    author='Arpit J',
    maintainer='Arpit J',
    description="Edit and source dotfiles directly from the terminal",
    scripts=['srcdit/srcdit.py'],
    entry_points = {
    'console_scripts': ['srcdit=srcdit:main'],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[#!/usr/bin/env python
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)