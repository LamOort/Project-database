echo off
set PATH=%PATH%;Y:\staff\_tka\PortableGit\bin;Y:\staff\_tka\python;Y:\staff\_tka\python\Scripts
echo python and git can be used now
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver 0.0.0.0:8280