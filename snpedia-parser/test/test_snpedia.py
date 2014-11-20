import sys
sys.path.append("./..")
import unittest
from snpedia import Snpedia

class TestSnpedia(unittest.TestCase):

    def setUp(self):
        self.snpedia = Snpedia()

    def test_get_snps(self):
        pass
        #snps = []
        #for snp in self.snpedia.get_snps():
        #    snps.append(snp)
        #    print snp
        #self.assertTrue(len(snps) > 0)

    def test_snp_info(self):
        #pass
        snp = "rs7412"
        results = self.snpedia.snp_info(snp)
        self.assertEqual(results['snp'], snp)
        self.assertEqual(results['orientation'], 'plus')

    def test_get_wikitext(self):
        pass
        #snp = "rs7412"
        #results = self.snpedia.get_wikitext(snp)
        #self.assertEqual(results["snp"], snp)
        #assert(len(results["wikitext"]) > 0)

    def test_expand_infobox(self):
        """docstring for test_expand_templates"""
        template = u"{{Rsnum\n|rsid=7412\n|Gene=APOE\n|Chromosome=19\n|position=44908822\n|Orientation=plus\n|ReferenceAllele=C\n|MissenseAllele=T\n|GMAF=0.07392\n|Assembly=GRCh38\n|GenomeBuild=38.1\n|dbSNPBuild=141\n|geno1=(C;C)\n|geno2=(C;T)\n|geno3=(T;T)\n|Gene_s=APOE\n}}': u'{{Rsnum\n|rsid=7412\n|Gene=APOE\n|Chromosome=19\n|position=44908822\n|Orientation=plus\n|ReferenceAllele=C\n|MissenseAllele=T\n|GMAF=0.07392\n|Assembly=GRCh38\n|GenomeBuild=38.1\n|dbSNPBuild=141\n|geno1=(C;C)\n|geno2=(C;T)\n|geno3=(T;T)\n|Gene_s=APOE\n}}"

        #res_json = {"expandtemplates":{"*":"[[Category:is a snp]][[Category:In dbSNP]]<div style=\"clear:right; float:right; margin-left:1em; margin-bottom:1em; max-width: 25em; text-align: left; font-size: 90%; border:thin solid;\"><table border=\"0\">\n<tr><td width=\"90\">[[Orientation]]</td><td>[[Orientation::plus]]</td></tr>\n</table>[[SMW::off]]\n{| class=\"sortable smwtable\" width=\"100%\"\n ! Geno \n ! [[Magnitude|Mag]] \n ! Summary\n |-\n\n| [[Rs7412(C;C)|(C;C)]] \n| style=\"background: #ff8080\" | 0 \n| more likely to gain weight if taking olanzapine\n|-\n\n| [[Rs7412(C;T)|(C;T)]] \n| style=\"background: #ffffff\" |  \n| more likely to gain weight if taking olanzapine\n|-\n\n| [[Rs7412(T;T)|(T;T)]] \n| style=\"background: #ffffff\" |  \n| normal\n|-\n\n|}\n[[SMW::on]]<table width=\"100%\" border=\"1\" style=\"border-collapse: collapse;\">\n\n\n\n</table>\n\n<table border=\"0\">\n<tr><td width=\"90\">Reference</td><td>[[Assembly::GRCh38]] [[GenomeBuild::38.1]]/[[DBSNPBuild::141]]</td></tr>\n</table><table border=\"0\">\n<tr><td width=\"90\">Chromosome</td><td>[[on chromosome::19]]</td></tr>\n[[Category:SNPs on chromosome 19]]\n</table><table border=\"0\">\n<tr><td width=\"90\">Position</td><td>[[chromosome position::44908822]]</td></tr>\n</table><table border=\"0\">\n<tr><td width=\"90\">Gene</td><td>[[In gene::APOE]]</td></tr>\n</table><table colspan=\"2\" width=\"100%\">\n<tr><td width=\"90\">is a</td><td>[[snp]]</td></tr>\n<tr><td>is</td><td>[[Special:Whatlinkshere/Rs7412 | mentioned by]]</td></tr>\n<tr><td>dbSNP</td><td>[http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=7412 rs7412]</td></tr>\n<tr><td>Exac</td><td>[http://exac.broadinstitute.org/dbsnp/rs7412 rs7412]</td></tr>\n<tr><td>PheGenI</td><td>[http://www.ncbi.nlm.nih.gov/gap/PheGenI?tab=2&rs=7412 rs7412]</td></tr>\n<tr><td>nextbio</td><td>[http://www.nextbio.com/b/search/snp/rs7412?type=snp&q0=rs7412&t0=snp#tab=populations rs7412]</td></tr>\n<tr><td>[[help (hapmap)|hapmap]]</td><td>[http://hapmap.ncbi.nlm.nih.gov/cgi-perl/gbrowse/hapmap27_B36/?name=SNP%3Ars7412 rs7412]</td></tr>\n<tr><td>[[1000 genomes]]</td><td>[http://browser.1000genomes.org/Homo_sapiens/Variation/Population?v=rs7412;vdb=variation rs7412]</td></tr>\n<tr><td>hgdp</td><td>[http://hgdp.uchicago.edu/cgi-bin/gbrowse/HGDP/?name=SNP%3Ars7412 rs7412]</td></tr>\n<tr><td>ensembl</td><td>[http://www.ensembl.org/Homo_sapiens/snpview?source=dbSNP;snp=rs7412 rs7412]</td></tr>\n<tr><td>gopubmed</td><td>[http://www.gopubmed.org/search?q=rs7412 rs7412]</td></tr>\n<tr><td>geneview</td><td>[http://bc3.informatik.hu-berlin.de/search?gv_search_query=RS:7412 rs7412]</td></tr>\n<tr><td>scholar</td><td>[http://scholar.google.com/scholar?q=rs7412&as_subj=bio rs7412]</td></tr>\n<tr><td>google</td><td>[http://www.google.com/search?hl=en&q=rs7412 rs7412]</td></tr>\n<tr><td>pharmgkb</td><td>[http://www.pharmgkb.org/rsid/rs7412 rs7412]</td></tr>\n<tr><td>gwascentral</td><td>[http://www.gwascentral.org/marker/dbSNP:rs7412 rs7412]</td></tr>\n<tr><td>openSNP</td><td>[http://opensnp.org/snps/rs7412 rs7412]</td></tr>\n<tr><td>[[23andMe (help)|23andMe]]</td><td>[https://www.23andme.com/you/explorer/snp/?snp_name=rs7412 rs7412]</td></tr>\n<tr><td>23andMe all</td><td>[https://www.23andme.com/you/search/?isearch=rs7412 rs7412]</td></tr>\n<tr><td>SNP Nexus</td><td><form action=\"http://snp-nexus.org/cgi-bin/snp/s5_63.cgi\" method=\"post\" ENCTYPE=\"multipart/form-data\">\n<input type=\"hidden\" name=\"dbsnp_id\" size=10 value=\"rs7412\">\n<input type=\"hidden\" name=\"email\" size=70 value=\"guest@snpedia.com\">\n<input type=\"hidden\" name=\"refseq\" value=\"refseq\">\n<input type=\"hidden\" name=\"ensembl\" value=\"ensembl\">\n<input type=\"hidden\" name=\"sift\" value=\"sift\">\n<!-- <input type=\"hidden\" name=\"acembly\" value=\"acembly\">\n<input type=\"hidden\" name=\"vega\" value=\"vega\"> -->\n<input type=\"hidden\" name=\"ucsc\" value=\"ucsc\">\n<input type=\"hidden\" name=\"ceu\" value=\"ceu\">\n<input type=\"hidden\" name=\"yri\" value=\"yri\">\n<input type=\"hidden\" name=\"chb\" value=\"chb\">\n<input type=\"hidden\" name=\"jpt\" value=\"jpt\">\n<input type=\"hidden\" name=\"tfbs\" value=\"tfbs\">\n<input type=\"hidden\" name=\"firstef\" value=\"firstef\">\n<input type=\"hidden\" name=\"mirbase\" value=\"mirbase\">\n<input type=\"hidden\" name=\"mirna\" value=\"mirna\">\n<input type=\"hidden\" name=\"mirna1\" value=\"mirna1\">\n<input type=\"hidden\" name=\"gad\" value=\"gad\">\n<input type=\"hidden\" name=\"lafrate\" value=\"lafrate\">\n<input type=\"hidden\" name=\"redon\" value=\"redon\">\n<input type=\"hidden\" name=\"sebat\" value=\"sebat\">\n<input type=\"hidden\" name=\"locke\" value=\"locke\">\n<input type=\"hidden\" name=\"sharp\" value=\"sharp\">\n<input type=\"hidden\" name=\"conrad\" value=\"conrad\">\n<input type=\"hidden\" name=\"hinds\" value=\"hinds\">\n<input type=\"hidden\" name=\"carroll\" value=\"carroll\">\n<input type=\"hidden\" name=\"tuzun\" value=\"tuzun\">\n<input type=\"submit\" value = \"rs7412\" >\n</form></td></tr>\n<tr><td>SNPshot</td><td>[http://bioai4core.fulton.asu.edu/snpshot/FactSheet?id=rs7412&type=RSNO rs7412]</td></tr>\n<tr><td>SNPdbe</td><td>[http://www.rostlab.org/services/snpdbe/dosearch.php?id=mutation&val=rs7412 rs7412]</td></tr>\n<tr><td>MSV3d</td><td>[http://decrypthon.igbmc.fr/msv3d/cgi-bin/humsavar?rsid=rs7412 rs7412]</td></tr>\n</table>[[Category:Has genotype]]<table border=\"0\">\n<tr><td width=\"90\">[[GMAF]]</td><td>[[GMAF::0.07392]]</td></tr>\n</table><table border=\"0\">\n<tr><td width=\"90\">[[Max Magnitude]]</td><td>[[Max Magnitude::0]]\n</td></tr>\n</table>\n</div>"}}
        data = self.snpedia.expand_infobox(template)
        self.assertEqual(data["orientation"], "plus")

    def parse_smwtable_wikitext(self):
        text = "{| class=\"sortable smwtable\" width=\"100%\"\n ! Geno \n ! [[Magnitude|Mag]] \n ! Summary\n |-\n\n| [[Rs7412(C;C)|(C;C)]] \n| style=\"background: #ff8080\" | 0 \n| more likely to gain weight if taking olanzapine\n|-\n\n| [[Rs7412(C;T)|(C;T)]] \n| style=\"background: #ffffff\" |  \n| more likely to gain weight if taking olanzapine\n|-\n\n| [[Rs7412(T;T)|(T;T)]] \n| style=\"background: #ffffff\" |  \n| normal\n|-\n\n|}"

        #records = self.snpedia.parse_smwtable_wikitext(wikitext)
        #self.assertEqual(len(records), 3)

if __name__ == '__main__':
    unittest.main()

