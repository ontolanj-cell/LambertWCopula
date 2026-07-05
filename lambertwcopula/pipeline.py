"""
Analysis Pipeline
=================

Coordinates the complete Lambert W Copula analysis.

Author: Jay Ontolan
"""

from .context import AnalysisContext

from .import_data import load_csv


class AnalysisPipeline:
    """
    Main analysis pipeline.
    """

    def __init__(self):

        self.context = AnalysisContext()

    @property
    def ctx(self):
        return self.context
    
    def load_data(self, filename):
        """
        Load a dataset into the analysis context.
        """

        self.context.data = load_csv(filename)

        return self.context.data