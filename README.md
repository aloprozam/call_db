# call_db
Project for learning Django and Python
--- ---

#### Local Testing
--- ---
Start local database in a Docker container
```shell
docker compose up -d
```
Stop local database with deleting data
```shell
docker compose down -v
```
Install project python dependencies
```python
pip -r ./requirements.txt
```
Apply migrations
```python
python .\manage.py migrate
```
Create superuser
```python
python .\manage.py createsuperuser
```