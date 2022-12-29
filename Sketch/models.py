from django.db import models
from django_range_slider.fields import RangeSliderField


class Images(models.Model):
    id = models.AutoField(primary_key=True)
    original_img = models.ImageField(
        upload_to='original/', null=True, verbose_name="Image")
    original_size = models.TextField(null=True)
    #quality = RangeSliderField(minimum=10, maximum=102, label="Quality ", name="quality")
    # quality = models.CharField( max_length=3, null=True)
    converted_img = models.ImageField(upload_to='converted/', null=True)
    converted_size = models.TextField(null=True)
