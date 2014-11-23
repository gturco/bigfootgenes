import json

from snpedia import Snpedia

class SnpediaStore:
    def __init__(self):
        self.snpedia = Snpedia()
        pass

    def create_db(self):
        """docstring for create_db"""
        pass

    def import_data(self, snp_data_file):
        """snp_data_file is created from \
        SnpediaFetcher.write_snp_wikitext_to_file"""

        with open(snp_data_file, 'r') as file:
            for line in file:
                mysql_insert_stmt = self.create_mysql_insert_stmt_from_snpedia_data_line(line)
                print mysql_insert_stmt


    def create_mysql_insert_stmt_from_snpedia_data_line(self, line):
        """docstring for create_mysql_insert_stmt_from_snpedia"""

        # snp_data = json.loads(line)

        snp_data = eval(line)
        snp = snp_data['snp']
        wikitext = snp_data['wikitext']

        record = self.snpedia.snp_info_from_wikitext(snp, wikitext)

        mysql_stmt = "";
        for geno in record['geno_records']:
            if len(geno) > 0:
                # TODO reverse complement the geno if orientation is negative
                #record['orientation']

                stmt = "INSERT INTO snps(rsid,genotype,summary) VALUES(\"{0}\",\"{1}\",\"{2}\");".format(snp, geno['Geno'], geno['Summary'])
                mysql_stmt += stmt;

        return mysql_stmt

    def query(self, rsid, genotype):
        """docstring for query"""
        pass
