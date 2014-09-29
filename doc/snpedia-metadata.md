# What the keys of the SNPedia sidebar means

orientation (plus|minus) refers to the strand.

# Getting info from the infobox
When we get the wikitext from a snp page like http://www.snpedia.com/index.php/Rs7412

We get the side infobox as
```
{{Rsnum|rsid=7412|Gene=APOE|Chromosome=19|position=44908822|Orientation=plus|ReferenceAllele=C|MissenseAllele=T|GMAF=0.07392|Assembly=GRCh38|GenomeBuild=38.1|dbSNPBuild=141|geno1=%28C;C%29|geno2=%28C;T%29|geno3=%28T;T%29|Gene_s=APOE}}
```

However, we want the summary info expanded like seen on the html page:
Geno 	Mag 	Summary
(C;C) 	0 	more likely to gain weight if taking olanzapine
(C;T) 		more likely to gain weight if taking olanzapine
(T;T) 		normal

We need to eval the infobox to get this info:

"http://bots.snpedia.com/api.php?action=expandtemplates&text={{Rsnum|rsid=7412|Gene=APOE|Chromosome=19|position=44908822|Orientation=plus|ReferenceAllele=C|MissenseAllele=T|GMAF=0.07392|Assembly=GRCh38|GenomeBuild=38.1|dbSNPBuild=141|geno1=%28C;C%29|geno2=%28C;T%29|geno3=%28T;T%29|Gene_s=APOE}}&format=xml"

This returns the formatted HTML page.

