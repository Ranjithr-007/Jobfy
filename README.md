
Django Job Portal.  

Install requirements

pip install -r requirements.txt

Database

Set the database from settings.py

To migrate the database open terminal in project directory and type

python manage.py makemigrations
python manage.py migrate

Collects all static files in your apps

python manage.py collectstatic

Run the server

python manage.py runserver
