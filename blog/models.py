from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='images/')

    def get_summary(self):
        return self.text[:20]


    def __str__(self):
        return self.title

    


