from setuptools import setup, find_packages
import glob
import os

this_directory = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name="showdata",
    version="1.4.8",
    author="Dechao Meng",
    url="https://github.com/silverbulletmdc/showdata",
    author_email="dechao.meng@vipl.ict.ac.cn",
    description="Remote file system visualizer and manager.",
    long_description_content_type="text/markdown",
    long_description=open("README.rst").read(),
    packages=find_packages(exclude=('examples', 'examples.*')),
    scripts=glob.glob('scripts/*'),
    install_requires=['click', 'pandas', 'flask', 'flask-cors']
)
