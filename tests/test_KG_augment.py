import unittest

import requests

from metrics.util import describe_loa
from metrics.util import describe_biotools
from metrics.util import describe_wikidata
from metrics.util import describe_opencitation
from metrics.util import is_DOI, get_DOI

from rdflib import Graph, ConjunctiveGraph, Namespace, URIRef, Literal, BNode


class KGAugmentTestCase(unittest.TestCase):
    def test_base_url(selfself):
        # from https://github.com/RDFLib/rdflib/issues/1003
        rdf_triples_base = """
        @prefix category: <http://example.org/> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @base <http://example.org/> .

        <> a skos:ConceptScheme ;
            dct:creator <https://creator.com> ;
            dct:description "Test Description"@en ;
            dct:source <nick> ;
            dct:title "Title"@en .
        """
        kg = ConjunctiveGraph()
        kg.parse(data=rdf_triples_base, format="turtle")
        print(kg.serialize(format="turtle").decode())

        rdf_triples_NO_base = """
        @prefix category: <http://example.org/> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        <> a skos:ConceptScheme ;
            dct:creator <https://creator.com> ;
            dct:description "Test Description"@en ;
            dct:source <nick> ;
            dct:title "Title"@en .
        """
        kg = ConjunctiveGraph()
        kg.parse(data=rdf_triples_NO_base, format="turtle")
        print(kg.serialize(format="turtle").decode())

        # from scratch
        kg2 = ConjunctiveGraph()
        kg2.add(
            (
                URIRef("http://fair-checker/example/qs"),
                URIRef("http://value"),
                Literal("2"),
            )
        )
        print(
            kg2.serialize(format="turtle", base="http://fair-checker/example/").decode()
        )

        kg3 = ConjunctiveGraph()
        kg3.parse(
            data="@base <http://example.org/> . <> a <http://example.org/Class> .",
            format="turtle",
        )
        kg3 = kg3 + kg2
        print(
            kg3.serialize(format="turtle", base="http://fair-checker/example/").decode()
        )

    @unittest.skip("To be done by a CRON")
    def test_wikidata_sparqlwrapper(self):
        # r2 = R2Impl()
        # r2.set_url("https://workflowhub.eu/workflows/45")
        # r2.extract_html_requests()
        # r2.extract_rdf()
        # kg = r2.get_jsonld()
        # print(len(kg))
        # print(kg)
        # print(kg.serialize(format='turtle').decode())

        url = "http://www.wikidata.org/entity/Q28665865"
        url = "https://search.datacite.org/works/10.7892/boris.108387"

        kg = ConjunctiveGraph()
        kg = describe_wikidata(url, kg)
        print(kg.serialize(format="turtle").decode())

    @unittest.skip("wikidata sparql endpoint access 403 error")
    def test_wikidata_http(self):
        endpoint = "https://query.wikidata.org/sparql"

        uri = "https://www.wikidata.org/entity/Q1684014"
        uri = "wd:Q1684014"
        h = {"Accept": "text/csv"}
        p = {"query": "'DESCRIBE " + uri + "'"}
        res = requests.get(endpoint, headers=h, params=p, verify=True)
        print(res.url)
        print(res)
        print(res.text)
        kg = ConjunctiveGraph()
        kg.parse(data=res.text, format="turtle")
        print(f"loaded {len(kg)} triples")
        self.assertEqual(49, len(kg))

    @unittest.skip("To be done by a CRON")
    def test_biotools(self):
        # r2 = R2Impl()
        # r2.set_url("https://workflowhub.eu/workflows/45")
        # r2.extract_html_requests()
        # r2.extract_rdf()
        # kg = r2.get_jsonld()
        # print(len(kg))
        # print(kg)
        # print(kg.serialize(format='turtle').decode())

        url = "http://www.wikidata.org/entity/Q28665865"
        url = "https://workflowhub.eu/workflows/45"
        url = "https://bio.tools/bwa"

        kg = ConjunctiveGraph()
        kg = describe_biotools(url, kg)
        print(kg.serialize(format="turtle").decode())

        # self.assertEqual(True, False)

    @unittest.skip("To be done by a CRON")
    def test_loa(self):
        # r2 = R2Impl()
        # r2.set_url("https://workflowhub.eu/workflows/45")
        # r2.extract_html_requests()
        # r2.extract_rdf()
        # kg = r2.get_jsonld()
        # print(len(kg))
        # print(kg)
        # print(kg.serialize(format='turtle').decode())

        url = "http://www.wikidata.org/entity/Q28665865"
        url = "https://workflowhub.eu/workflows/45"
        url = "https://search.datacite.org/works/10.7892/boris.108387"

        # check if id or doi in uri
        if is_DOI(url):
            uri = get_DOI(url)
            print(f"FOUND DOI: {uri}")
            # describe on lod.openair
            kg = ConjunctiveGraph()
            kg = describe_loa(uri, kg)
            print(kg.serialize(format="turtle").decode())

        # self.assertEqual(True, False)

    # @unittest.skip("To be done by a CRON")
    def test_opencitation(self):
        # r2 = R2Impl()
        # r2.set_url("https://workflowhub.eu/workflows/45")
        # r2.extract_html_requests()
        # r2.extract_rdf()
        # kg = r2.get_jsonld()
        # print(len(kg))
        # print(kg)
        # print(kg.serialize(format='turtle').decode())

        url = "http://www.wikidata.org/entity/Q28665865"
        url = "https://doi.pangaea.de/10.1594/PANGAEA.914331"
        url = "https://search.datacite.org/works/10.7892/boris.108387"

        kg = ConjunctiveGraph()
        kg = describe_opencitation(url, kg)
        print(kg.serialize(format="turtle").decode())

        # self.assertEqual(True, False)

    @unittest.skip("To be done by a CRON")
    def test_all(self):
        # r2 = R2Impl()
        # r2.set_url("https://workflowhub.eu/workflows/45")
        # r2.extract_html_requests()
        # r2.extract_rdf()
        # kg = r2.get_jsonld()
        # print(len(kg))
        # print(kg)
        # print(kg.serialize(format='turtle').decode())

        url = "http://www.wikidata.org/entity/Q28665865"
        url = "https://doi.pangaea.de/10.1594/PANGAEA.914331"
        url = "https://search.datacite.org/works/10.7892/boris.108387"
        url = "https://bio.tools/bwa"

        kg = ConjunctiveGraph()
        kg = describe_loa(url, kg)
        kg = describe_opencitation(url, kg)
        kg = describe_wikidata(url, kg)
        kg = describe_biotools(url, kg)
        print(kg.serialize(format="turtle").decode())

        # self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
