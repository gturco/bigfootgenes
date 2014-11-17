from snpedia import Snpedia

class SnpediaFetcher:
    def __init__(self):
        """docstring for __init__"""
        self.snpedia = Snpedia()

    def write_all_snps(self, filepath):
        """Get all the snp names"""
        with open(filepath, 'w') as file:
            for snp in self.snpedia.get_snps():
                file.write("{}\n".format(snp))

    def write_snp_wikitext_to_file(self, snps, filepath):
        """get the wikitext for the snps array"""

        with open(filepath, 'w') as file:
            for snp in snps:
                trimmed_snp = snp.strip()
                if trimmed_snp:
                    print trimmed_snp
                    result = self.snpedia.get_wikitext(trimmed_snp)
                    file.write("{}\n".format(result))

