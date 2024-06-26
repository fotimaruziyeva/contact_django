from django.db import models

# BLOG- title,description,photo,datetime
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='Blog/image')
    description=models.TextField()
    published_date=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.title}  by {self.author}"
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} by {self.email}"
        