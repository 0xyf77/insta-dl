from setuptools import setup, find_packages

setup(
    name='insta-reel-downloader',
    version='0.1.0',
    description='A Python library to download Instagram reels',
    packages=find_packages(),
    install_requires=['instaloader'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
