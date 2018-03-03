echo off
set PATH=%PATH%;Y:\staff\_tka\PortableGit\bin;Y:\staff\_tka\python;Y:\staff\_tka\python\Scripts
echo python and git are now available
git clone -b Project-e1400487 https://github.com/LamOort/Project_database.git
echo the project has been cloned to your current folder
python -m pip install djangorestframework-xml
python -m pip install djangorestframework-jsonapi
echo frameworks have been installed
echo installation has been completed