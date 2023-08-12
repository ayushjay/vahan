# Vahan
Generate a score for each vehicle by performing sentiment analysis on scraped, crowdsourced reviews

1. Clone this project
```
https://github.com/ayushjay/vahan.git
```
2. Move into the cloned project directory
```
cd vaahan
```
3. Create a virtual env
```
python3 -m venv env

source env/bin/activate
```
4. Install the requirements
```
pip install -r requirements.txt
```
5. Make database migrations
```
python3 manage.py makemigrations

python3 manage.py migrate
```
6. Run the vaahan application
```
python3 manage.py runserver
```

