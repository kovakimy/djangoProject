from django.db import models


class Records(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    master = models.CharField('Master', max_length=20)
    client = models.CharField('Client', max_length=20)

    def __str__(self):
        return str([self.time, self.master, self.client])

    class Meta:
        verbose_name = 'RecordNails'
        verbose_name_plural = 'RecordsNails'


class RecordsEyebrows(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    master = models.CharField('Master', max_length=20)
    client = models.CharField('Client', max_length=20)

    def __str__(self):
        return str([self.time, self.master, self.client])

    class Meta:
        verbose_name = 'RecordEyebrows'
        verbose_name_plural = 'RecordsEyebrows'


class RecordsEyelashes(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    master = models.CharField('Master', max_length=20)
    client = models.CharField('Client', max_length=20)

    def __str__(self):
        return str([self.time, self.master, self.client])

    class Meta:
        verbose_name = 'RecordEyelashes'
        verbose_name_plural = 'RecordsEyelashes'


class Feedback(models.Model):
    client = models.CharField('Client', max_length=20)
    master = models.CharField('Master', max_length=20)
    feedback = models.TextField('Feedback')