from metrics.AbstractFAIRMetrics import AbstractFAIRMetrics
from metrics.F2B_Impl import F2B_Impl


class I2_Impl(AbstractFAIRMetrics):

    """
    GOAL :

    """

    def __init__(self, web_resource):
        super().__init__(web_resource)
        # self.name = "I2"
        self.id = "8"
        self.principle = "https://w3id.org/fair/principles/terms/I2"
        self.principle_tag = "I2"
        self.implem = "FAIR-Checker"
        self.desc = ""

    def weak_evaluate(self) -> bool:
        """
        Delegated to F2B
        """
        return F2B_Impl(self.get_web_resource()).weak_evaluate()

    def strong_evaluate(self) -> bool:
        """
        Delegated to F2B
        """
        return F2B_Impl(self.get_web_resource()).strong_evaluate()
