from optparse import OptionParser
from snpedia_fetcher import SnpediaFetcher

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="read a INFILE", metavar="INFILE")


    parser.add_option("-o", "--output", dest="output",
                      help="write to OUTFILE", metavar="OUTFILE")

    (options, args) = parser.parse_args()

    fetcher = SnpediaFetcher()

    if not options.input:
        parser.error("Missing input")

    if not options.output:
        parser.error("Missing output")

    with open(options.input) as f:
        snps = f.readlines()
        if len(snps) > 0:
            fetcher.write_snp_wikitext_to_file(snps, options.output)
        else:
            print "input file was empty"

if __name__ == '__main__':
    main()

