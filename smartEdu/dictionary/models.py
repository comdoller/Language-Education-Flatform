from django.db import models

class Dictionary(models.Model):
    dNO = models.IntegerField(db_column='dNO', primary_key=True)
    tCODE = models.IntegerField(db_column='tCODE')
    dTetum = models.CharField(db_column='dTetum', max_length=128)
    dEnglish = models.CharField(db_column='dEnglish', max_length=128)
    dBahasa = models.CharField(db_column='dBahasa', max_length=128)
    dKorea = models.CharField(db_column='dKorea', max_length=128)
    dJapan = models.CharField(db_column='dJapan', max_length=128)


    class Meta:
        managed = False
        db_table = 'Dictionary'

    def __str__(self):
        return ""