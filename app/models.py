from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    
    url=models.URLField()
    email=models.EmailField(max_length=100,default='email2027@gmail.com')
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.url
    def __str__(self):
        return self.email

    def __str__(self):
        return self.name
    

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    
    def __str__(self):
        return self.date
    def __str__(self):
        return self.author