from django.db import models

from django.contrib.auth.models import User
'''Pointer
Here a model is created that is a table in db and fields are defined where default for complete is set , and created is added automatically
also __str__ is used so that when 
tasks = Task.objects.all() is called it doesnt show as  Task object (1) but as the title of it 

we can use below if i want to show according to status of complete
    def __str__(self) :
        return f"{self.complete}"

'''
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) :
        return f"{self.title}"
