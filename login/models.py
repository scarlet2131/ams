# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class professor(models.Model):
    name = models.TextField(blank=False)
    professor_id = models.AutoField(primary_key=True)
    password = models.TextField(max_length=254,blank=False)
    email = models.EmailField(max_length=254,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
	

