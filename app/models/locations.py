from django.db import models


class Sido(models.Model):
    sidoCd = models.CharField(max_length=7, primary_key=True)
    sidoNm = models.CharField(max_length=20)


class Sigungu(models.Model):
    sidoCd = models.ForeignKey("Sido", on_delete=models.CASCADE)
    sigunguCd = models.CharField(max_length=7, primary_key=True)
    sigunguNm = models.CharField(max_length=20)


