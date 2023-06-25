from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField('Name:',max_length=150)
    surname = models.CharField('Surname:',max_length=150)
    email = models.EmailField('Email')
    pay = models.BooleanField('To\'ladi/To\'lamadi', default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    class Meta:
        ordering = ['-id']




