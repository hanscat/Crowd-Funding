from haystack.indexes import *
from .models import Report

class ReportIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    owner = CharField(model_attr='owner')
    title = CharField(model_attr='title')
    company = CharField(model_attr='company')
    ceo = CharField(model_attr='ceo')
    sector = CharField(model_attr='sector')
    industry = CharField(model_attr='industry')
    location = CharField(model_attr='location')
    country = CharField(model_attr='country')
    projects = CharField(model_attr='projects')
    projects2 = CharField(model_attr='projects2')
    projects3 = CharField(model_attr='projects3')
    projects4 = CharField(model_attr='projects4')
    projects5 = CharField(model_attr='projects5')



    def get_model(self):
        return Report

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
