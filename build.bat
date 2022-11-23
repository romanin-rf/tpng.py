@echo off
python setup.py bdist_wheel
twine upload dist/*