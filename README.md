# viewsets project

# this is just a crud project using modelviewset and modelserializer

# to clone this repository

git clone https://github.com/vinayakyan/project_13_02_2024.git

cd project_13_02_2024

py -m virtualenv venv

venv\Scripts\activate - for windows
venv/bin/activate - for linux/MacOS

cd viewsets_project

pip install -r requirements.txt

py manage.py makemigrations

py manage.py migrate

py manage.py runserver
