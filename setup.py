import pathlib

import pkg_resources
import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Deep Learning Plus',
    version='0.0.6',
    author='Greenfrogs',
    author_email='5961364+greenfrogs@users.noreply.github.com',
    description='A collection of Python packages designed for the Python 3.9 for when you only want 1 import',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/greenfrogs/DeepLearningPlus',
    license='Apache License 2.0',
    install_requires=[
        'tqdm==4.62.3',
        'h5py==3.6.0',
        'matplotlib==3.5.1',
        'pytorch-lightning==1.5.7',
        'opencv-python==4.5.4.60',
        'scipy==1.7.3'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.9.*',
)