from django.db import models
# Create your models here.
class testtable(models.Model):
    Id=models.IntegerField()
    Name=models.CharField(max_length=20)
    class Meta:
        db_table="testtable"
