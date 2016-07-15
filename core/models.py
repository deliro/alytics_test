from django.db import models
from django.db.models import Q


class DataSet(models.Model):
    input = models.TextField()
    result = models.TextField(null=True)
    exception = models.CharField(max_length=200, null=True)

    @property
    def done(self):
        return bool(self.result or self.exception)

    @property
    def no_errors(self):
        return not self.exception

    @classmethod
    def get_last_status(cls):
        obj = cls.objects.filter(Q(result__isnull=False) | Q(exception__isnull=False)).order_by('-pk').first()
        if obj is None:
            return 'False'
        return str(obj.exception is not None)
