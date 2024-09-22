from django.db import models


class report_model(models.Model):
    work_time = models.FloatField()
    vt184_t = models.IntegerField()
    vt184_f = models.IntegerField()
    vt044_1_t = models.IntegerField()
    vt044_1_f = models.IntegerField()
    vt044_2_t = models.IntegerField()
    vt044_2_f = models.IntegerField()
    fix105_1_t = models.IntegerField()
    fix105_1_f = models.IntegerField()
    fix105_2_t = models.IntegerField()
    fix105_2_f = models.IntegerField()
    g206_t = models.IntegerField()
    g206_f = models.IntegerField()
    top_t = models.IntegerField()
    top_f = models.IntegerField()
