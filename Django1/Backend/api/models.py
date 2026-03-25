
# Create your models here.
# You created a Django model called Note → it represents a database table.
# Imports
from django.db import models
from django.contrib.auth.models import User

# Model Declaration
class Note(models.Model): # Create a table named Note in the database
    #Fields (Columns in DB)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")#forign key

    def __str__(self):#to read this
        return self.title