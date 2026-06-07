from django.db import models


class Provinsi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'provinces'

    def __str__(self):
        return self.name


class Regencies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    province_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'regencies'

    def __str__(self):
        return self.name


class Districts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    regency_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'districts'

    def __str__(self):
        return self.name


class Villages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    district_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'villages'

    def __str__(self):
        return self.name