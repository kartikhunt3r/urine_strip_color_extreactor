from django.db import models

class UrineStrip(models.Model):
    strip_image = models.ImageField(upload_to='strips/')
    analysis_result = models.JSONField(null=True, blank=True)
