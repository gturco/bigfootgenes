from optparse import OptionParser
from snpedia_store import SnpediaStore

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="read a INFILE", metavar="INFILE")

    parser.add_option("-o", "--output", dest="output",
                      help="write to OUTFILE", metavar="OUTFILE")

    (options, args) = parser.parse_args()

    store = SnpediaStore()

    if not options.input:
        parser.error("Missing input")

    if not options.output:
        parser.error("Missing output")

    store.write_mysql_insert_file(options.input, options.output)

if __name__ == '__main__':
    # example
    # python bigfootgenes/write_mysql_insert_file.py -i data/wikitext/snp-aa -o data/mysql/insert-snp-aa.sql
    main()
