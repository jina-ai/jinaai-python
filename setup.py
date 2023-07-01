from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='jinaai',
    version='0.2.0',
    author='Jina AI',
    author_email='guillaume.roncari@jina.ai',
    description='Jina AI Python SDK',
    url='https://github.com/jina-ai/jinaai-py.git',
    packages=find_packages(),
    install_requires=[
        'requests',
        'base64',
        'mimetypes',
        'os',
        're'
    ],
    long_description=README,
    long_description_content_type='text/markdown', 
)
