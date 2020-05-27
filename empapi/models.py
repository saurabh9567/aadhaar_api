from django.db import models

# Create your models here.
class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    uan = models.CharField(max_length=20)
    check_id = models.CharField(max_length=20, null=True)
    candidate_fname = models.CharField(max_length=50, null=True)               #  name format??
    candidate_mname = models.CharField(max_length=50, null=True)
    candidate_lname = models.CharField(max_length=50, null=True)
    date_of_joining = models.DateField(null=True)
    date_of_releiving = models.DateField(null=True)
    company_name = models.CharField(max_length=200, null=True)           #one or multiple company 
    client_id = models.CharField(max_length=100, null=True)
    client_name = models.CharField(max_length=200, null=True)
    status_code = models.IntegerField(default=0, null=True)
    consent = models.CharField(max_length=5, null=True)             # 0--->NO, 1--->YES
    request_json = models.CharField(max_length=250, null=True) 


class Uan_response(models.Model):
    id = models.AutoField(primary_key=True)
    uan = models.CharField(max_length=20)
    check_id = models.CharField(max_length=20, null=True)
    candidate_fname = models.CharField(max_length=50, null=True)               #  name format??
    candidate_mname = models.CharField(max_length=50, null=True)
    candidate_lname = models.CharField(max_length=50, null=True)
    date_of_joining = models.DateField(null=True)
    date_of_releiving = models.DateField(null=True)
    company_name = models.CharField(max_length=200, null=True)           #one or multiple company 
    request_json = models.CharField(max_length=250, null=True)
    response_json = models.CharField(max_length=250, null=True)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=100, null=True)
    client_name = models.CharField(max_length=200, null=True)
    date_of_joining = models.DateField(null=True)
    date_of_releiving = models.DateField(null=True)


class Match_result(models.Model):
    check_id = models.CharField(max_length=20, null=True)
    name_match = models.BooleanField(default=False, null=True)
    doj_match = models.BooleanField(default=False, null=True)
    dor_match = models.BooleanField(default=False, null=True)
    company_match = models.BooleanField(default=False, null=True)


class SessionModel(models.Model):
    count = models.IntegerField(default=0)

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)


class ModelWithImage(models.Model):
    image = models.ImageField(
        upload_to='images',
    )