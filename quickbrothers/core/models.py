from django.db import models
from django.dispatch import receiver
import os


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    address = models.TextField(verbose_name="Address")
    duration = models.CharField(max_length=255, verbose_name="Project durantion")

    def __str__(self):
        return self.name


def custom_upload_to(instance, filename):
    return '{}/{}'.format(instance, filename)


class ProjectImage(models.Model):
    image = models.FileField(upload_to = custom_upload_to)
    project = models.ForeignKey('Project', related_name='get_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.project.name



@receiver(models.signals.post_delete, sender=ProjectImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        # verifica si existe el archivo en el sistema
        if os.path.isfile(instance.image.path):
            #borra la imagen del disco duro del sistema
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ProjectImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        return False

    # trata busca el nombre de la imagen actual
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    # Guarda en una variable el nombre de la nueva imagen
    new_file = instance.image
    # Verifica si es la misma imagen
    if not old_file == new_file:
        # verifica si existe la ruta al archivo
        if os.path.isfile(old_file.path):
            # borra la vieja imagen
            os.remove(old_file.path)