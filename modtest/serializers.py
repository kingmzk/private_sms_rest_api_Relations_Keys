from rest_framework import serializers
from .models import Accelerator, OptyTracker, OptyAcc, Competation,OppCompetation,Microservice,OppMicroservice


class AcceleratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Accelerator
        fields =  ['acc_name']


class OptyTrackerSerializer(serializers.ModelSerializer):
    accelerators = serializers.SerializerMethodField()
    competations = serializers.SerializerMethodField()
    microservices = serializers.SerializerMethodField()

    class Meta:
        model = OptyTracker        
        fields = ['op_id', 'op_name', 'client_name', 'accelerators', 'competations', 'microservices']

    def get_accelerators(self, obj):
        mylist = []
        for accelerator in obj.accelerators.all():
            mylist.append(accelerator.acc_name)
        return ", ".join(mylist)
    
    def get_competations(self, obj):
        mylist = []
        for competation in obj.Competations.all():
            mylist.append(competation.name)
        return ", ".join(mylist)

    def get_microservices(self, obj):
        mylist = []
        for microservice in obj.Microservices.all():
            mylist.append(microservice.name)
        return ", ".join(mylist)

    

class OptyAccSerializer(serializers.ModelSerializer):
    opty_id = OptyTrackerSerializer(read_only=True)
    acc_id = AcceleratorSerializer(read_only=True)

    class Meta:
        model = OptyAcc
        fields = '__all__'


class CompetationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competation
        fields = '__all__'

class OppCompetationSerializer(serializers.ModelSerializer):
    opty_id = OptyTrackerSerializer(read_only=True)
    comp_id = CompetationSerializer(read_only=True) 
    
    class Meta:
        model = OppCompetation
        fields = '__all__'
        
class MicroserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microservice
        fields = '__all__'
        
class OppMicroserviceSerializer(serializers.ModelSerializer):
    opty_id = OptyTrackerSerializer(read_only=True)
    micro_id = MicroserviceSerializer(read_only=True)
    
    class Meta:
        model = OppMicroservice
        fields = '__all__'