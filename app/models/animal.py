from django.db import models


class KindCd(models.Model):
    kindCd = models.CharField(max_length=6, primary_key=True)
    kindNm = models.CharField(max_length=10)