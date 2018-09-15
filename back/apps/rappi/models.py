from django.db import models


class Storekeepers(models.Model):
    storekeeper_id = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    lng = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    toolkit = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'storekeepers'
