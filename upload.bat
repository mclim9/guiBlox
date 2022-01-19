python setup.py sdist
set datestr=%date:~10,4%.%date:~4,2%.%date:~7,2%
echo %datestr%
python -m unittest -v test.test_guiblox_import
python -m unittest -v test.test_project_import
twine upload .\dist\guiblox-*.tar.gz