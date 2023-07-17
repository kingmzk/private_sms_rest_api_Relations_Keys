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
        read_only_fields = ['op_id', 'op_name', 'client_name']

    def get_accelerators(self, obj):
        return list(obj.accelerators.values_list('acc_name', flat=True))

    def get_competations(self, obj):
        return list(obj.Competations.values_list('name', flat=True))

    def get_microservices(self, obj):
        return list(obj.Microservices.values_list('name', flat=True))

    

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