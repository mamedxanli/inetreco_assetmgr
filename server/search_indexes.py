# Haystack imports
from haystack import indexes

# Import from our apps
from server.models import Server

class ServerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #decomissioned = indexes.BooleanField(model_attr='decomissioned')
    brand = indexes.CharField(model_attr='brand')
    #server_model = indexes.CharField(model_attr='server_model')
    generation = indexes.CharField(model_attr='generation')
    #manufacture_year = indexes.IntegerField(model_attr='manufacture_year')
    serial_number = indexes.CharField(model_attr='serial_number')
    os = indexes.CharField(model_attr='os')
    #warranty = indexes.CharField(model_attr='warranty')
    #server_cpu = indexes.CharField(model_attr='server_cpu')
    #server_ram = indexes.CharField(model_attr='server_ram')
    #local_storage = indexes.CharField(model_attr='local_storage')
    other = indexes.CharField(model_attr='other')

    def get_model(self):
        return Server

    def index_queryset(self, using=None):
        return self.get_model().objects.all()