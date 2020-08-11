from django.db import models
from django.urls import reverse

class Ebook(models.Model):
    eNo = models.IntegerField(db_column='eNo',db_index=True, primary_key=True)
    eName = models.CharField(db_column='eName', max_length=128)
    eData = models.CharField(db_column='eData', max_length=1000)

    class Meta:
        managed = False
        db_table = 'Ebook'


    def __str__(self):
        return "eNo : " + self.eNo + " eName : " + self.Name + " eData : " + self.Data
