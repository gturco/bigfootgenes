# Bigfootgenes

@sudogenes

## Prereqs

Python 2.7.X

On Ubuntu 14.04

```
sudo apt-get install git python-dev python-pip wget libxml2 libxml2-dev libxslt-dev
sudo apt-get install mysql-server
```

```
pip install wikitools beautifulsoup4 requests mwparserfromhell flask

pip install mysql-connector-python --allow-external mysql-connector-python

pip install -i http://pypi.pediapress.com/simple/ mwlib
```

## Database

```
mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development
```

## Run data processing

```
mysql -uroot -p < data/mysql/schema.sql
```

```
cd bigfootgenes
```

```
python write_snp_names.py -f ../data/snps.txt
```

```
split -l 5000 snps.txt snp-
```

```
time python write_snp_wikitext.py -i ../data/snps-split/snp-aa -o ../data/wikitext/snp-aa
```

```
time python import_snps_to_mysql.py -i ../data/wikitext/snp-aa > aa.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ab > ab.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ac > ac.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ad > aa.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ae > ae.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-af > af.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ag > ag.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ah > ah.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ai > ai.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-aj > aj.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ak > ak.log
time python import_snps_to_mysql.py -i ../data/wikitext/snp-al > al.log
```

```
time python write_23andme_report.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -o ../data/genome_tommy_chheng_snp_matches.txt
```

## Webapp

### Setup

Second, let's download `pip`, `virtualenv`, `foreman`, and the [`heroku`
Ruby gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt

### Running Your Application

Now, you can run the application locally.

    $ python app.py

On the server you can use gunicorn :

    $ sudo gunicorn --log-level=info --log-file=bigfootgenes.log -w 2 -b 0.0.0.0:80 --timeout 600 app:app

Long timeout because of long upload times. TOFIX by placing nginx in
front.

Setup gunicorn/nginx on centos7
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7
