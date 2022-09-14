from django.db import models



class Students(models.Model):
    student_name=models.CharField(max_length=300)
    age = models.IntegerField()
    number = models.IntegerField()

    # class Meta:
    #     ordering=['-publishedon']
    #     verbose_name_plural='Books'
    

    # def __str__(self):
    #     return '{}        {}'.format(self.book_name, self.publishedon)
# Create your models here.
