import sys

sys.path.insert(1, "..")

import unittest
import json
import requests
from rdflib import ConjunctiveGraph, Graph
from metrics.util import ask_OLS, ask_LOV

# from metrics.util import ask_BioPortal

import random


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        print("STARTING all tests")

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        print("ENDING all tests")

    @unittest.skip("To be done by a CRON")
    def test_OLS(self):
        uri1 = "https://bio.tools/bwa"
        self.assertFalse(ask_OLS(uri1))
        uri2 = "http://schema.org/Organization"
        self.assertFalse(ask_OLS(uri2))
        uri3 = "http://www.ebi.ac.uk/efo/EFO_0000001"
        self.assertTrue(ask_OLS(uri3))

    @unittest.skip("To be done by a CRON")
    def test_LOV(self):
        uri1 = "https://bio.tools/bwa"
        self.assertFalse(ask_LOV(uri1))
        uri2 = "http://schema.org/Organization"
        self.assertTrue(ask_LOV(uri2))
        uri3 = "http://www.ebi.ac.uk/efo/EFO_0000001"
        self.assertFalse(ask_LOV(uri3))

    @unittest.skip("To be done by a CRON")
    def testMetricsAPI(sefl):
        print(f"call to the FAIRMetrics API")
        api_url = (
            "https://fair-evaluator.semanticscience.org/FAIR_Evaluator/metrics.json"
        )

        h = {"Accept": "application/json"}
        res = requests.get(api_url, headers=h, verify=False)

        # if res.json() > 0:
        #     return True
        # else:
        #     return False

    @unittest.skip("To be done by a CRON")
    def testGen2UniqueIdentifier(self):
        smarturl = "https://w3id.org/FAIR_Tests/tests/gen2_unique_identifier"
        doi = "10.5281/zenodo.1147435"
        print(f"call to the FAIRMetrics API for [ {doi} ]")

        h = {"Accept": "application/json"}
        data = '{"subject": "' + doi + '"}'
        data = data.encode("utf-8")
        res = requests.post(smarturl, headers=h, params=data)
        print(res)


class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)


if __name__ == "__main__":
    unittest.main()
