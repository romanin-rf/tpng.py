import os
import setuptools

setuptools.setup(
    name='tpng.py',
    version='0.1.2',
    description='A special file format for displaying images in the terminal.',
    keywords='tpng.py',
    packages=setuptools.find_packages(),
    author_email='semina054@gmail.com',
    url="https://github.com/romanin-rf/tpng.py",
    zip_safe=False,
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    author='ProgrammerFromParlament',
    license='MIT',
    requires=["pillow"]
)