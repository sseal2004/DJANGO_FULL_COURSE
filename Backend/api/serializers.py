from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#ORM
# a built-in tool that allows developers to interact with a relational database using Python code instead of writing raw SQL

#Using this serializers for accepting new user and defining a new user 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','id','username','password']
        extra_kwargs={'password':{"write_only":True}}#only accept password but donot return password

    def create(self,validate_data):
        user=User.objects.create_user(**validate_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}