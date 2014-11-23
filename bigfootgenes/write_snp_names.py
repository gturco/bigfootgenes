from optparse import OptionParser
from snpedia_fetcher import SnpediaFetcher

def main():
    parser = OptionParser()
    parser.add_option("-o", "--output", dest="output",
                      help="write to [OUTFILE]", metavar="OUTFILE")

    (options, args) = parser.parse_args()

    fetcher = SnpediaFetcher()

    if not options.output:
        parser.error("Missing output")

    fetcher.write_all_snps(options.output)

if __name__ == '__main__':
    main()
