def parse_23andme_file(file_path):
    data = open(file_path)
    return data

def parse_23andme_data(data):
    for dna_line in data:
        if dna_line[0] == "#": continue
        rsid,chromosome,position,genotype = dna_line.strip().split("\t")
