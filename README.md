<img src="gallery_1375157.png" alt="drawing" width="100" height="100"/>

# Gallery Project for Mate Academy
Simple CRUD application for managing art pieces and authors.

## Check it out
(ㅅ´ ˘ `) ✧
https://gallery-mate.onrender.com

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

![gallery drawio](https://github.com/mariiahorbova/gallery-mate/assets/44654425/cd0df434-9f7b-4b6b-a73b-57b9d61c97cc)

![image](https://github.com/mariiahorbova/gallery-mate/assets/44654425/9768e15c-7221-4d99-8c3c-ca46fdf693ec)


