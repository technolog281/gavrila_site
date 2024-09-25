from django.db import models


class report_model(models.Model):
    vt184_t = models.IntegerField()
    vt184_f = models.IntegerField()
    vt184_i = models.IntegerField()
    vt184_p = models.IntegerField()

    vt044_1_t = models.IntegerField()
    vt044_1_f = models.IntegerField()
    vt044_1_i = models.IntegerField()
    vt044_1_p = models.IntegerField()

    vt044_2_t = models.IntegerField()
    vt044_2_f = models.IntegerField()
    vt044_2_i = models.IntegerField()
    vt044_2_p = models.IntegerField()

    fix105_1_t = models.IntegerField()
    fix105_1_f = models.IntegerField()
    fix105_1_i = models.IntegerField()
    fix105_1_p = models.IntegerField()

    fix105_2_t = models.IntegerField()
    fix105_2_f = models.IntegerField()
    fix105_2_i = models.IntegerField()
    fix105_2_p = models.IntegerField()

    g206_t = models.IntegerField()
    g206_f = models.IntegerField()
    g206_i = models.IntegerField()
    g206_p = models.IntegerField()

    top_1_t = models.IntegerField()
    top_1_f = models.IntegerField()
    top_1_i = models.IntegerField()
    top_1_p = models.IntegerField()

    top_2_t = models.IntegerField()
    top_2_f = models.IntegerField()
    top_2_i = models.IntegerField()
    top_2_p = models.IntegerField()

    date = models.DateField()
    tg_id = models.CharField()
    name = models.CharField()
    work_time = models.FloatField()
    day_total = models.FloatField()
    day_total_s = models.FloatField()
    day_total_time = models.FloatField()

