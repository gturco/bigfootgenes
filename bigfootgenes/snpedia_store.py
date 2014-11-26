import json
import mysql.connector

from mysql.connector import errorcode
from snpedia import Snpedia

class SnpediaStore:
    def __init__(self):
        self.snpedia = Snpedia()

        self.config = {
          'user': 'bigfootgenes',
          'password': 'dk34DFko99FDOQ',
          'host': '127.0.0.1',
          'database': 'bigfootgenes_development',
          'raise_on_warnings': True
        }

        # get the mysql cursor
        self.cnx = mysql.connector.connect(**self.config)

    def query(self, rsid, genotype):
        """Query snps given a rsid and genotype"""
        query = ("SELECT rsid, genotype, summary FROM snps "
                 "WHERE rsid = %s AND genotype = %s")

        cursor = self.cnx.cursor()
        cursor.execute(query, (rsid, genotype))

        for (rsid, genotype, summary) in cursor:
            record = {'rsid': rsid, 'genotype': genotype, 'summary': summary}
            yield record

        cursor.close()

    def import_snps(self, snp_data_file):
        """snp_data_file is created from write_snp_wikitext_to_file.py"""

        with open(snp_data_file, 'r') as input_file:
            for line in input_file:
                try:
                    self.insert_snp(line)
                except Exception:
                    print "Error inserting: {0}\n" % line

    def insert_snp(self, line):
        """line is created from write_snp_wikitext.py"""

        # TODO when we switch the data format to real json, use json.loads instead of eval
        # snp_data = json.loads(line)
        snp_data = eval(line)

        snp = snp_data['snp']
        wikitext = snp_data['wikitext']

        record = self.snpedia.snp_info_from_wikitext(snp, wikitext)

        if not record.has_key('geno_records'):
            return ""

        cursor = self.cnx.cursor()

        for geno in record['geno_records']:
            if len(geno) > 0:
                stmt = u"""INSERT INTO snps(rsid,genotype,summary) VALUES(?, ?, ?);"""
                cursor.execute(query, (snp, geno['Geno'], geno['Summary']))

        cursor.close()

    def write_mysql_insert_file(self, snp_data_file, mysql_output_file):
        """snp_data_file is created from \
        SnpediaFetcher.write_snp_wikitext_to_file"""

        with open(mysql_output_file, 'w') as output_file:
            with open(snp_data_file, 'r') as input_file:
                for line in input_file:
                    # TODO add try-except to ignore errors
                    mysql_insert_stmt = self.create_mysql_insert_stmt_from_snpedia_data_line(line)
                    if mysql_insert_stmt:
                        output_file.write(mysql_insert_stmt + "\n")

    def create_mysql_insert_stmt_from_snpedia_data_line(self, line):
        """docstring for create_mysql_insert_stmt_from_snpedia"""

        # TODO when we switch the data format to real json, use json.loads instead of eval
        # snp_data = json.loads(line)
        snp_data = eval(line)

        snp = snp_data['snp']
        wikitext = snp_data['wikitext']

        record = self.snpedia.snp_info_from_wikitext(snp, wikitext)

        if not record.has_key('geno_records'):
            return ""

        mysql_stmt = "";
        for geno in record['geno_records']:
            if len(geno) > 0:
                escaped_summary = geno['Summary'].replace("\"", "\\\"")
                stmt = u"""INSERT INTO snps(rsid,genotype,summary) VALUES("{0}","{1}","{2}");""".format(snp, geno['Geno'], escaped_summary)
                mysql_stmt += stmt;

        return mysql_stmt
