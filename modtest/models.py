'''
from django.db import models

class Accelerator(models.Model):
    id = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=255)

    def __str__(self):
        return self.acc_name


class OptyTracker(models.Model):
    id = models.AutoField(primary_key=True)
    op_id = models.IntegerField()
    op_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return self.op_name


class OptyAcc(models.Model):
    opty_id = models.ForeignKey(OptyTracker, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Accelerator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Opty ID: {self.opty_id_id}, Acc ID: {self.acc_id_id}"

'''

'''
from django.db import models

class Accelerator(models.Model):
    acc_name = models.CharField(max_length=255)

    def __str__(self):
        return self.acc_name


class OptyTracker(models.Model):
    op_id = models.IntegerField()
    op_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return self.op_name


class OptyAcc(models.Model):
    opty_id = models.ForeignKey(OptyTracker, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Accelerator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Opty ID: {self.opty_id_id}, Acc ID: {self.acc_id_id}"
'''


'''from django.db import models

class Accelerator(models.Model):
    acc_name = models.CharField(max_length=255)

    def __str__(self):
        return self.acc_name


class OptyTracker(models.Model):
    op_id = models.IntegerField()
    op_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    accelerators = models.ManyToManyField(Accelerator, through='OptyAcc')

    def __str__(self):
        return self.op_name


class OptyAcc(models.Model):
    opty_id = models.ForeignKey(OptyTracker, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Accelerator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Opty ID: {self.opty_id_id}, Acc ID: {self.acc_id_id}"
'''




from django.db import models
from django.forms import ValidationError

class Accelerator(models.Model):
    id = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=255)

    def __str__(self):
        return self.acc_name
    
    
class Competation(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Microservice(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name  


class OptyTracker(models.Model):
    id = models.AutoField(primary_key=True)
    op_id = models.IntegerField(unique=True)
    op_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    accelerators = models.ManyToManyField(Accelerator, through='OptyAcc')
    Competations = models.ManyToManyField(Competation, through='OppCompetation')
    Microservices = models.ManyToManyField(Microservice, through='OppMicroservice')

    def __str__(self):
        return self.op_name


class OptyAcc(models.Model):
    id = models.AutoField(primary_key=True)
    opty_id = models.ForeignKey(OptyTracker, on_delete=models.CASCADE)
    acc_id = models.ForeignKey(Accelerator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Opty ID: {self.opty_id_id}, Acc ID: {self.acc_id_id}"


class OppCompetation(models.Model):
    opty_id = models.ForeignKey(OptyTracker,on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Competation,on_delete=models.CASCADE)


class OppMicroservice(models.Model):
    opty_id = models.ForeignKey(OptyTracker,on_delete=models.CASCADE)
    micro_id = models.ForeignKey(Microservice,on_delete=models.CASCADE)
    
    

def save_model(instance):
    try:
        instance.full_clean()  # Validate model fields
        instance.save()  # Save the model
    except ValidationError as e:
        # Handle validation error
        print(f"Validation error occurred: {e}")