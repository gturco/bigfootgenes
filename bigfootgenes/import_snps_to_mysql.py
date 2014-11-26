from optparse import OptionParser
from snpedia_store import SnpediaStore

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="read a INFILE", metavar="INFILE")

    (options, args) = parser.parse_args()

    if not options.input:
        parser.error("Missing input")

    store = SnpediaStore()

    store.import_snps(options.input)

if __name__ == '__main__':
    # example
    # python import_snps_to_mysql.py -i ../data/wikitext/snp-aa
    main()

