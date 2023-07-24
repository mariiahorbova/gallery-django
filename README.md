![project_logo](https://github.com/mariiahorbova/gallery-mate/blob/main/gallery_1375157.png?raw=true)

# Gallery Project for Mate Academy
Simple CRUD application for managing art pieces and authors.

### Entities:
1. User
2. Genre
3. ArtPiece
4. Gallery

## Setup
​
1. Clone the project:
```
git clone https://github.com/mariiahorbova/gallery-mate.git
```
2. Navigate to the project directory:
```
cd gallery-mate
```
3. Create .env file in gallery-mate directory and populate it with variables (see .env.example)
4. Create virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```
5. Install dependencies
```
pip install -r requirements.txt
```
6. Apply migrations to the project
```
python manage.py migrate
```
7. Create superuser to login
```
python manage.py createsuperuser
```
8. Start server
```
python manage.py runserver
```

## Accessing the Application
​
* The Django application is accessible at `http://localhost:8000/`

​Remember to replace `localhost` with the relevant IP address if you're not accessing these from the same machine where the services are running.

