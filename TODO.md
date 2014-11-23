# TODO:

# TASKs:

## python-app:

*  Parse 23andme file
*  Parse SNPedia from web
*  Create maping into mysql
*    Fix strand bug
*    Need to group SNPs of same catorgy

# Uses:

* Import 23andme data
*   1) parses the file
*   2) maps your snps
*   3) seperate by:
*     Good and Bad
*     Risk level up and down X

in 23andme data:

rsid	chromosome	position	genotype
rs4477212	1	82154	AA
rs3094315	1	752566	AA

check snpedia's data for rs4477212

if orientation is plus

else if orientation is negative
reverse complement the AA 23andme

A => T
G => C
C => G
T => A

and flip

example:
GT => CA => AC

## Database

rsid     genotype  summary
Rs7412   CC        "XXX"
Rs7412   CT        "XXX"

# Results:

* Visulize
