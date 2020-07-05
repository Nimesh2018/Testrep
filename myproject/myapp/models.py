from django.db import models
# Create your models here.
class testtable(models.Model):
    Id=models.IntegerField()
    Name=models.CharField(max_length=20)
    class Meta:
        db_table="testtable"

class posttable(models.Model):
    Emp_id=models.AutoField(primary_key=True)
    Emp_name=models.CharField(max_length=20)
    class Meta:
        db_table="posttable"
    def _str_(self):
        return self.Emp_name 
