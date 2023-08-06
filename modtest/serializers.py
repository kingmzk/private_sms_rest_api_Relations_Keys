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

    def validate_op_id(self, value):
        if value < 0:
            raise serializers.ValidationError("op_id must be a positive integer")
        return value

    def validate(self, data):
        accelerators_data = data.get('accelerators')
        competations_data = data.get('competations')
        microservices_data = data.get('microservices')

        if not accelerators_data:
            raise serializers.ValidationError("At least one accelerator must be provided")
        if not competations_data:
            raise serializers.ValidationError("At least one competation must be provided")
        if not microservices_data:
            raise serializers.ValidationError("At least one microservice must be provided")

        return data

    

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
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        DECLARE @optytracker_id INT = 1;

-- Get the ID of the OptyTracker instance
SELECT @optytracker_id = id FROM dbo.modtest_optytracker WHERE op_id = @optytracker_id;

-- Clear existing many-to-many relations for Competations
DELETE FROM dbo.modtest_oppcompetation WHERE opty_id_id = @optytracker_id;

-- Insert new Competation relations
INSERT INTO dbo.modtest_oppcompetation (opty_id_id, comp_id_id)
SELECT @optytracker_id, id
FROM dbo.modtest_competation
WHERE name IN ('infosys', 'MY Company');










-- Insert new Competation relations
INSERT INTO dbo.modtest_competation (name)
SELECT DISTINCT name
FROM (VALUES ('Infosys'), ('MY Company')) AS new_comps (name)
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.modtest_competation c
    WHERE LOWER(c.name) = LOWER(new_comps.name)
);

-- Insert relations into modtest_oppcompetation
INSERT INTO dbo.modtest_oppcompetation (opty_id_id, comp_id_id)
SELECT @optytracker_id, c.id
FROM dbo.modtest_competation c
WHERE LOWER(c.name) IN ('infosys', 'my company');


        '''