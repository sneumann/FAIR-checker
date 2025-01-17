from metrics.AbstractFAIRMetrics import AbstractFAIRMetrics
from metrics.Evaluation import Evaluation
from metrics.test_metric import testMetric, requestResultSparql


class FAIRMetricsImpl(AbstractFAIRMetrics):
    def __init__(self, name, id, desc, api, principle, creator, created_at, updated_at):
        self.name = name
        self.id = id
        self.desc = desc
        self.api = api
        self.implem = "FAIRMetrics"
        self.principle = principle
        self.creator = creator
        self.created_at = created_at
        self.updated_at = updated_at

    def get_api(self):
        return self.api

    def evaluate(self, url) -> Evaluation:
        data = '{"subject": "' + url + '"}'
        print("Evaluating " + self.name)

        eval = Evaluation()
        eval.set_start_time()
        eval.result_text = testMetric(self.api, data)
        eval.set_end_time()
        eval.set_score(requestResultSparql(eval.result_text, "ss:SIO_000300"))
        eval.set_reason(requestResultSparql(eval.result_text, "schema:comment"))
        # principle are URLs so we get the last element after the last /
        eval.set_metrics(self.principle.split("/")[-1])
        eval.set_target_uri(url)
        eval.persist()

        return eval

    def weak_evaluate(self) -> bool:
        pass

    def strong_evaluate(self) -> bool:
        pass
