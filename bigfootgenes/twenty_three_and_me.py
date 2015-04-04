import os, zipfile
from snpedia_store import SnpediaStore

class TwentyThreeAndMe():
    def __init__(self):
        """docstring for __init__"""
        self.snpedia_store = SnpediaStore()

    def parse_23andme_file(self, file_path):
        # handle both zip and unzipped files

        abs_file_path = os.path.abspath(file_path)

        if zipfile.is_zipfile(abs_file_path):
            zf = zipfile.ZipFile(abs_file_path)
            for file in zf.namelist():
                try:
                    zf.extract(file, "/tmp")
                    tmp_path = os.path.join("/tmp", file)
                    data = open(tmp_path)
                    os.remove(tmp_path)

                    return data
                except KeyError:
                    raise 'ERROR unzipping file'
        else:
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


