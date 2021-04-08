from django.db import models

class todo(models.Model):
    title = models.TextField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        # return '%s: %s' % (self.id, self.title)
        return self.title
    