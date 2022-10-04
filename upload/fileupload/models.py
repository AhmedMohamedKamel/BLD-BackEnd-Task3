from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    timedate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timedate)

