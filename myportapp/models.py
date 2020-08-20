from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='projects/')
    project_link = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.project_name


class TechUsed(models.Model):
    project = models.ForeignKey(Project, related_name="techused",on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=100)


    def __str__(self):
        return '%s' % (self.tech_name)



    

class Skills(models.Model):
    skill_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='skills/')
    description= models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


