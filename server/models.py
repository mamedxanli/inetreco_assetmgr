#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/netdev/<>/<filename>
    return '{0}/{1}/{2}'.format("server", instance.pk, filename)

class Server(models.Model):
    # Timestamps
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #created_by = models.CharField(max_length=100, default=None)

    # Model
    brand = models.CharField("Brand", max_length=20)
    server_model = models.CharField("Model", max_length=20)
    generation = models.CharField("Generation", max_length=5)
    manufacture_year = models.IntegerField("Year of manufacture")
    serial_number = models.CharField("Serial number", max_length=20)
    os = models.CharField("Operating system", blank=True, max_length=100, default=None)
    warranty = models.CharField("Warranty status", blank=True, max_length=100)
    server_cpu = models.CharField("Server CPU", max_length=100)
    server_ram = models.CharField("Server RAM", max_length=100)
    local_storage = models.CharField("Local storage", max_length=100)
    file_picture_1 = models.FileField("Front Picture",blank=True, default=None, upload_to=save_directory_path)
    file_picture_2 = models.FileField("Back Picture",blank=True, default=None, upload_to=save_directory_path)
    file_other = models.FileField("Other file/Zip file if many", blank=True, default=None, upload_to=save_directory_path)
    other = models.TextField("Notes", blank=True, max_length=10000)


    def __str__(self):
        return " {}, IP {}".format(self.pk, self.serial_number)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('server_detail', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('server_detail', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Server"
        return class_name

    class Meta:
        verbose_name_plural = "Servers"
