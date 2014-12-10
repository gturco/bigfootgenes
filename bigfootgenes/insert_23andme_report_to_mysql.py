import json
import mysql.connector
import logging

from contextlib import closing
from mysql.connector import errorcode

from optparse import OptionParser
from twenty_three_and_me import TwentyThreeAndMe

def write_user_snp_to_mysql(userid, matches):
    config = {
      'user': 'bigfootgenes',
      'password': 'dk34DFko99FDOQ',
      'host': '127.0.0.1',
      'database': 'bigfootgenes_development',
      'raise_on_warnings': True
    }

    # get the mysql cursor
    cnx = mysql.connector.connect(**config)

    stmt = u"""INSERT INTO user_snps(userid, rsid, genotype, summary) VALUES(%s, %s, %s, %s);"""
    with closing(cnx.cursor()) as cur:
        for match in matches:
            values = (userid, match['rsid'], match['genotype'], match['summary'])
            cur.execute(stmt, values)
        print "Inserted {0} rows".format(len(matches))
    cnx.commit()
    
def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="read a INFILE", metavar="INFILE")
    parser.add_option("-u", "--userid", dest="userid",
                      help="The id associated with the report", metavar="USERID")


    (options, args) = parser.parse_args()

    if not options.input:
        parser.error("Missing input")

    if not options.userid:
        parser.error("Missing userid")

    twenty_three_and_me = TwentyThreeAndMe()

    data = twenty_three_and_me.parse_23andme_file(options.input)
    matches = twenty_three_and_me.get_snp_matches(data)

    write_user_snp_to_mysql(options.userid, matches)

if __name__ == '__main__':
    # example
    # python insert_23andme_report_to_mysql.py -i ../data/genome_Tommy_Chheng_Full_20140920095607.txt -u afsd34
    main()

