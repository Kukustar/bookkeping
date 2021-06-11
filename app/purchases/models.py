from django.db import models

class Purchase(models.Model):
    date = models.DateTimeField('purchase date time')
    cost = models.FloatField(default=0.0)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)

class Balance(models.Model):
    mount = models.FloatField(default=0.0)
    name = models.CharField(blank=True, max_length=200)

    def return_mount_after_delete(self, mount):
        self.mount = self.mount + mount
        self.save()

    def remove_mount_after_create(self, mount):
        self.mount = self.mount - mount
        self.save()