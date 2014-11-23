from snpedia_store import SnpediaStore

class TwentyThreeAndMe():
    def __init__(self):
        """docstring for __init__"""
        self.snpedia_store = SnpediaStore()

    def parse_23andme_file(self, file_path):
        data = open(file_path)
        return data

    def get_snp_matches(self, data):
        matches = []
        for dna_line in data:
            if dna_line[0] == "#": continue
            rsid,chromosome,position,genotype = dna_line.strip().split("\t")

            for result in self.snpedia_store.query(rsid, genotype):
                matches.append(result)

        return matches


