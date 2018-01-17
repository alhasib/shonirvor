# স্বনির্ভর - স্বনির্ভর বাংলাদেশ গড়ার পত্যয়ে

## install postgre sql
```
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
```

## install Psycopg2
```
pip install psycopg2
```
## change postgres conf
```
sudo nano /etc/postgresql/9.6/main/pg_hba.conf
```

change the line to
```
host all all 127.0.0.1/32 trust
```

## create database
```
sudo su – postgres
createdb money_dev_db
exit
```