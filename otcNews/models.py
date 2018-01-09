from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    ticker = models.CharField(unique=True, max_length=45)
    company_name = models.TextField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otc_company'

class OtcSecurities(models.Model):
    security_id = models.AutoField(primary_key=True)
    symbol = models.CharField(unique=True, max_length=45)
    trading_venue = models.CharField(max_length=45, blank=True, null=True)
    trading_date = models.TextField(blank=True, null=True)
    otc_tier = models.CharField(db_column='OTC_tier', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    caveat = models.CharField(max_length=45, blank=True, null=True)
    security_type = models.CharField(max_length=45, blank=True, null=True)
    security_class = models.CharField(max_length=45, blank=True, null=True)
    security_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    company_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otc_securities'

class OtcNews(models.Model):
    news_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()
    headline = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    url_hash = models.CharField(unique=True, max_length=100)
    ticker = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'otc_news'