from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    # Atributo 'objects' para el administrador (manager)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    # Atributo 'objects' para el administrador (manager)
    objects = models.Manager()

    def __str__(self):
        return str(self.title + ' - ' + self.project.name)
