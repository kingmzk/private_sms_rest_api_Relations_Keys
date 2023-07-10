'''
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Accelerator, OptyTracker, OptyAcc
from .serializers import AcceleratorSerializer, OptyTrackerSerializer, OptyAccSerializer
'''
'''
@api_view(['GET'])
def get_opportunity(request, pk=None):
    if pk is not None:
        try:
            opt = OptyTracker.objects.get(pk=pk)
            serializer = OptyTrackerSerializer(opt)
            opty_accs = OptyAcc.objects.filter(opty_id=pk)
            acc_names = [opty_acc.acc_id.acc_name for opty_acc in opty_accs]
            opt_data = serializer.data
            opt_data['acc_names'] = acc_names
            return Response(opt_data, status=status.HTTP_200_OK)
        except OptyTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        query = "SELECT * FROM api_optytracker"
        emp = OptyTracker.objects.raw(query)
        serializer = OptyTrackerSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_opportunity(request, pk=None):
    if pk is not None:
        try:
            opt = OptyTracker.objects.get(pk=pk)
            serializer = OptyTrackerSerializer(opt)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OptyTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        queryset = OptyTracker.objects.all()
        serializer = OptyTrackerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import OptyTracker, OptyAcc, Accelerator
# from .serializers import OptyTrackerSerializer


# @api_view(['GET'])
# def get_opportunity(request, pk=None):
#     if pk is not None:
#         try:
#             opt = OptyTracker.objects.get(pk=pk)
#             opt_data = {
#                 'id': opt.id,
#                 'op_id': opt.op_id,
#                 'op_name': opt.op_name,
#                 'client_name': opt.client_name,
#             }
#             opty_accs = OptyAcc.objects.filter(opty_id=pk)
#             accelerator_names = [opty_acc.acc_id.acc_name for opty_acc in opty_accs]
#             opt_data['accelerators'] = accelerator_names
#             return Response(opt_data, status=status.HTTP_200_OK)
#         except OptyTracker.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         query = OptyTracker.objects.all()
#         serializer = OptyTrackerSerializer(query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)





class AcceleratorViewSet(viewsets.ModelViewSet):
    queryset = Accelerator.objects.all()
    serializer_class = AcceleratorSerializer


class OptyTrackerViewSet(viewsets.ModelViewSet):
    queryset = OptyTracker.objects.all()
    serializer_class = OptyTrackerSerializer


class OptyAccViewSet(viewsets.ModelViewSet):
    queryset = OptyAcc.objects.all()
    serializer_class = OptyAccSerializer
'''





from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Accelerator, OptyTracker, OptyAcc, Competation, OppCompetation, Microservice, OppMicroservice
from .serializers import AcceleratorSerializer, OptyTrackerSerializer, OptyAccSerializer, CompetationSerializer, OppCompetationSerializer, MicroserviceSerializer, OppMicroserviceSerializer
from rest_framework.views import APIView



@api_view(['GET'])
def get_opportunity(request, pk=None):
    if pk is not None:
        try:
            opt = OptyTracker.objects.get(pk=pk)
            serializer = OptyTrackerSerializer(opt)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OptyTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        queryset = OptyTracker.objects.all()
        serializer = OptyTrackerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class OptyTrackerAPIView(APIView):
    def post(self, request):
        data = request.data

        # Extract the related data from the request
        accelerators_data = data.pop('accelerators', None)
        competations_data = data.pop('competations', None)
        microservices_data = data.pop('microservices', None)

        # Split the provided data into separate lists
        accelerators_list = [x.strip() for x in accelerators_data.split(',') if x.strip()]
        competations_list = [x.strip() for x in competations_data.split(',') if x.strip()]
        microservices_list = [x.strip() for x in microservices_data.split(',') if x.strip()]

        # Create or retrieve the related models and update the data
        accelerators = []
        for accelerator_name in accelerators_list:
            accelerator, _ = Accelerator.objects.get_or_create(acc_name=accelerator_name)
            accelerators.append(accelerator)

        competations = []
        for competation_name in competations_list:
            competation, _ = Competation.objects.get_or_create(name=competation_name)
            competations.append(competation)

        microservices = []
        for microservice_name in microservices_list:
            microservice, _ = Microservice.objects.get_or_create(name=microservice_name)
            microservices.append(microservice)

        # Check for existing values in the database
        existing_accelerators = Accelerator.objects.filter(acc_name__in=accelerators_list)
        existing_competations = Competation.objects.filter(name__in=competations_list)
        existing_microservices = Microservice.objects.filter(name__in=microservices_list)

        accelerators.extend(existing_accelerators)
        competations.extend(existing_competations)
        microservices.extend(existing_microservices)

        opty_data = {
            'op_id': data['op_id'],
            'op_name': data['op_name'],
            'client_name': data['client_name'],
        }

        # Save the OptyTracker model instance
        opty_tracker = OptyTracker.objects.create(**opty_data)

        # Set the many-to-many relations
        opty_tracker.accelerators.set(accelerators)
        opty_tracker.Competations.set(competations)
        opty_tracker.Microservices.set(microservices)

        serializer = OptyTrackerSerializer(opty_tracker)
        return Response(serializer.data, status=status.HTTP_201_CREATED)









class AcceleratorViewSet(viewsets.ModelViewSet):
    queryset = Accelerator.objects.all()
    serializer_class = AcceleratorSerializer


class OptyTrackerViewSet(viewsets.ModelViewSet):
    queryset = OptyTracker.objects.all()
    serializer_class = OptyTrackerSerializer


class OptyAccViewSet(viewsets.ModelViewSet):
    queryset = OptyAcc.objects.all()
    serializer_class = OptyAccSerializer


class CompetationViewSet(viewsets.ModelViewSet):
    queryset = Competation.objects.all()
    serializer_class = CompetationSerializer


class OppCompetationViewSet(viewsets.ModelViewSet):
    queryset = OppCompetation.objects.all()
    serializer_class = OppCompetationSerializer


class MicroserviceViewSet(viewsets.ModelViewSet):
    queryset = Microservice.objects.all()
    serializer_class = MicroserviceSerializer


class OppMicroserviceViewSet(viewsets.ModelViewSet):
    queryset = OppMicroservice.objects.all()
    serializer_class = OppMicroserviceSerializer
