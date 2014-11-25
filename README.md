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
python write_snp_wikitext.py -i ../data/snps_test.txt -o ../data/snps_test_wikitext.txt
```

```
time python write_mysql_insert_file.py -i ../data/wikitext/snp-aa -o ../data/mysql/insert-snp-aa.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ab -o ../data/mysql/insert-snp-ab.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ac -o ../data/mysql/insert-snp-ac.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ad -o ../data/mysql/insert-snp-ad.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ae -o ../data/mysql/insert-snp-ae.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-af -o ../data/mysql/insert-snp-af.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ag -o ../data/mysql/insert-snp-ag.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ah -o ../data/mysql/insert-snp-ah.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ai -o ../data/mysql/insert-snp-ai.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-aj -o ../data/mysql/insert-snp-aj.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-ak -o ../data/mysql/insert-snp-ak.sql
time python write_mysql_insert_file.py -i ../data/wikitext/snp-al -o ../data/mysql/insert-snp-al.sql
```

```
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-aa.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ab.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ac.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ad.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ae.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-af.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ag.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ah.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ai.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-aj.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-ak.sql
time mysql -ubigfootgenes -pdk34DFko99FDOQ bigfootgenes_development < ../data/mysql/insert-snp-al.sql
```

```
python write_23andme_report.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -o ../data/genome_tommy_chheng_snp_matches.txt
```
