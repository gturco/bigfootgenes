# Bigfootgenes

@sudogenes

## Prereqs

```
pip install wikitools BeautifulSoup requests mwparserfromhell
pip install -i http://pypi.pediapress.com/simple/ mwlib
```


## Run

```
python snpedia-parser/write_snp_names.py -f data/snps.txt
```

```
split -l 5000 snps.txt snp-
```

```
time python snpedia-parser/write_snp_wikitext.py -i data/snps-split/snp-aa -o data/wikitext/snp-aa
```

python snpedia-parser/write_snp_wikitext.py -i data/snps_test.txt -o data/snps_test_wikitext.txt
