from optparse import OptionParser
from twenty_three_and_me import TwentyThreeAndMe
import json

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="read a INFILE", metavar="INFILE")

    parser.add_option("-o", "--output", dest="output",
                      help="write to OUTFILE", metavar="OUTFILE")

    (options, args) = parser.parse_args()

    if not options.input:
        parser.error("Missing input")

    if not options.output:
        parser.error("Missing output")

    twenty_three_and_me = TwentyThreeAndMe()

    data = twenty_three_and_me.parse_23andme_file(options.input)
    matches = twenty_three_and_me.get_snp_matches(data)

    with open(options.output, 'w') as file:
        for match in matches:
            file.write("{}\n".format(json.dumps(match)))

if __name__ == '__main__':
    # example
    # python write_twenty_three_and_me_report.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -o ../data/genome_tommy_chheng_snp_matches.txt
    main()
