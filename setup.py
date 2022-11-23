import os
import setuptools

setuptools.setup(
    name='tpng.py',
    version='0.2.1',
    description='A special file format for displaying images in the terminal.',
    keywords='tpng.py',
    packages=setuptools.find_packages(),
    author_email='semina054@gmail.com',
    url="https://github.com/romanin-rf/tpng.py",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    author='programmer-from-parlament',
    license='MIT',
    requires=["pillow", "rich"],
    setup_requires=["pillow", "rich"]
)