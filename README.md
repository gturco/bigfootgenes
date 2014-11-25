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
python write_mysql_insert_file.py -i ../data/wikitext/snp-aa -o ../data/mysql/insert-snp-aa.sql
```

```
python write_twenty_three_and_me_report.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -o ../data/genome_tommy_chheng_snp_matches.txt
```
