from re import T
from django.db import models

# Create your models here.


class User(models.Model): 
    """
    entity for the various users of the system
    """
    id = models.AutoField(primary_key=True, unique=True)
    Fname = models.CharField(max_length=20, null = False)
    Lname = models.CharField(max_length=20, null=False)  


class Experience(models.Model): 
    """
    Entity for Dalice's experience
    """
    comp_name = models.CharField(primary_key=True, null=False, max_length=200)
    job_title = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    job_description = models.CharField(max_length=500)
    manager_contact = models.CharField(max_length=300, null=True)



class Skill(models.Model): 
    """
    Entity for Dalice's skills
    """
    skill_name = models.CharField(primary_key=True, max_length=200)
    proficiency_level = models.CharField(max_length=200)
    additional_details = models.CharField(max_length=200)


class Project(models.Model): 
    """
    Entity for Dalice's projects
    """
    project_name = models.CharField(primary_key=True, max_length=200)
    description = models.CharField(max_length=200)
    # Might need to add more on relevant links and documentation for each project.
    # IE I need proof.
    # Page with pictures of projects. 


class Certification(models.Model): 
    """
    Entity for Dalice's certitifications
    """
    cert_name = models.CharField(primary_key=True, max_length=200)
    issuing_org = models.CharField(max_length=200)
    completion_date = models.DateField(null=True)
    additional_details = models.CharField(max_length=200)


class Education(models.Model): 
    """
    Entity for Dalice's education
    """
    institution_name = models.CharField(primary_key=True, max_length=200)
    degree = models.CharField(max_length=200)
    field_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_details = models.CharField(max_length=200)



class Volunteer(models.Model):
    """
    Entity for Dalice's volunteer experience
    """
    organization = models.CharField(primary_key=True, max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    skills = models.CharField(max_length=200)


# Class representing a comment.
class Blog(models.Model): 
    """
    entity for additional comments

    accessed by only PM?
    """
    id = models.AutoField(primary_key=True, unique=True)
    entry_name = models.CharField(max_length=1000, null=True)
    body = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    blog_desc = models.CharField(max_length=300, null=True)
    #Date needs to be updated each time the comment is updated. 
    #auto_now = True should work
    updated_date = models.DateTimeField(auto_now=True, null=True)



# Maybe add a class for aws projects. 
# Definately adding a template for aws projects. 










