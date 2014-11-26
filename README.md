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
pip install wikitools beautifulsoup4 requests mwparserfromhell

pip install mysql-connector-python --allow-external mysql-connector-python

pip install -i http://pypi.pediapress.com/simple/ mwlib
```

## Run

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
time python import_snps_to_mysql.py -i ../data/wikitext/snp-aa
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ab
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ac
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ad
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ae
time python import_snps_to_mysql.py -i ../data/wikitext/snp-af
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ag
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ah
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ai
time python import_snps_to_mysql.py -i ../data/wikitext/snp-aj
time python import_snps_to_mysql.py -i ../data/wikitext/snp-ak
time python import_snps_to_mysql.py -i ../data/wikitext/snp-al
```

```
time python write_23andme_report.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -o ../data/genome_tommy_chheng_snp_matches.txt
```
