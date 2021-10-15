import logging
from rdflib import URIRef
from urllib.parse import urlparse
from metrics.AbstractFAIRMetrics import AbstractFAIRMetrics


class I3_Impl(AbstractFAIRMetrics):
    """
    GOAL :

    """

    def __init__(self, web_resource):
        super().__init__(web_resource)
        # self.name = "I3"
        self.id = "11"
        self.principle = "https://w3id.org/fair/principles/terms/I3"
        self.principle_tag = "I3"
        self.implem = "FAIR-Checker"
        self.desc = ""

    def weak_evaluate(self) -> bool:
        pass

    def strong_evaluate(self) -> bool:
        """at least 3 different URL authorities in URIs"""
        eval = self.get_evaluation()
        kg = self.get_web_resource().get_rdf()
        domains = []
        for s, p, o in kg:
            for term in [s, o]:
                if isinstance(term, URIRef):
                    parsed_url = urlparse(term)
                    if parsed_url.netloc not in domains:
                        domains.append(parsed_url.netloc)

        logging.debug(f"Domain names found in URis: {domains}")

        if len(domains) > 3:
            return eval.set_score(2)
        else:
            return eval.set_score(0)
