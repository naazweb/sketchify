## Sketchify
Checkout Live https://sketchify.pythonanywhere.com/
![Video of the site](https://github.com/naazweb/sketchify/blob/main/sample.gif?raw=true)

### Description
This web app is build with Django - Python Web Framework. It converts images into pencil sketch uisng OpenCV library. 

### Setup Locally
1. Clone Repository and checkout to `dev` branch.

    `git clone https://github.com/naazweb/sketchify`

    `cd sketchify` (move to the repo)

    `git checkout dev`
2. Setup virtual environment

    `python -m venv env` 
   
    or
    
    `virtualenv env`
3. Activate virtual environment

    `env/scripts/activate`

    or Linux / Mac
    
    `source env/bin/activate`
4. Install requirements

    `pip install -r requirements.txt`
5. Migrate and Run

    `python manage.py migrate`

    `python manage.py runserver`

6. Server will be up at http://127.0.0.1:8000/

Note: Don't forget to checkout to `dev` branch. The `main` branch is having paths specific to PythonAnywhere environment.

##### Thanks for stopping by ^ __ ^