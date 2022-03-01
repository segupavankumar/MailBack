from django.db import models

# Create your models here.

class UserMail(models.Model):
    id = models.BigAutoField(primary_key=True)
    FromMail = models.EmailField()
    ToMail = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    # Status = models.BooleanField(default=False)
    Date = models.TimeField()

    def __str__(self):
        return f'{self.FromMail} send to {self.ToMail}'
