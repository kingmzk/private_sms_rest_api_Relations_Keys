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




# @api_view(['GET'])
# def get_opportunity(request, pk=None):
#     if pk is not None:
#         try:
#             opt = OptyTracker.objects.get(pk=pk)
#             serializer = OptyTrackerSerializer(opt)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except OptyTracker.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         queryset = OptyTracker.objects.all()
#         serializer = OptyTrackerSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)




from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_opportunity(request, pk=None):
    if pk is not None:
        opt = get_object_or_404(OptyTracker, pk=pk)
        serializer = OptyTrackerSerializer(opt)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        queryset = OptyTracker.objects.all().only('op_id', 'op_name', 'client_name')
        serializer = OptyTrackerSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# import pyodbc
# from django.db import connection
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import OptyTracker
# from .serializers import OptyTrackerSerializer

# @api_view(['GET'])
# def get_opportunity(request, pk=None):
#     try:
#         with connection.cursor() as cursor:
#             if pk is not None:
#                 cursor.execute("SELECT * FROM dbo.optytracker WHERE id = %s", [pk])
#                 row = cursor.fetchone()
#                 if row is None:
#                     return Response(status=status.HTTP_404_NOT_FOUND)
#                 optytracker = {
#                     'op_id': row[0],
#                     'op_name': row[1],
#                     'client_name': row[2]
#                     # Add other fields as needed
#                 }
#                 serializer = OptyTrackerSerializer(data=optytracker)
#             else:
#                 cursor.execute("SELECT op_id, op_name, client_name FROM dbo.optytracker")
#                 rows = cursor.fetchall()
#                 optytrackers = []
#                 for row in rows:
#                     optytracker = {
#                         'op_id': row[0],
#                         'op_name': row[1],
#                         'client_name': row[2]
#                         # Add other fields as needed
#                     }
#                     optytrackers.append(optytracker)
#                 serializer = OptyTrackerSerializer(data=optytrackers, many=True)

#             if serializer.is_valid():
#                 serialized_data = serializer.data
#                 return Response(serialized_data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     except Exception as e:
#         return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)







# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_data = data.pop('accelerators', None)
#         competations_data = data.pop('competations', None)
#         microservices_data = data.pop('microservices', None)

#         # Split the provided data into separate lists
#         accelerators_list = [x.strip() for x in accelerators_data.split(',') if x.strip()]
#         competations_list = [x.strip() for x in competations_data.split(',') if x.strip()]
#         microservices_list = [x.strip() for x in microservices_data.split(',') if x.strip()]

#         # Create or retrieve the related models and update the data
#         accelerators = []
#         for accelerator_name in accelerators_list:
#             accelerator, _ = Accelerator.objects.get_or_create(acc_name=accelerator_name)
#             accelerators.append(accelerator)

#         competations = []
#         for competation_name in competations_list:
#             competation, _ = Competation.objects.get_or_create(name=competation_name)
#             competations.append(competation)

#         microservices = []
#         for microservice_name in microservices_list:
#             microservice, _ = Microservice.objects.get_or_create(name=microservice_name)
#             microservices.append(microservice)

#         # Check for existing values in the database
#         existing_accelerators = Accelerator.objects.filter(acc_name__in=accelerators_list)
#         existing_competations = Competation.objects.filter(name__in=competations_list)
#         existing_microservices = Microservice.objects.filter(name__in=microservices_list)

#         accelerators.extend(existing_accelerators)
#         competations.extend(existing_competations)
#         microservices.extend(existing_microservices)

#         opty_data = {
#             'op_id': data['op_id'],
#             'op_name': data['op_name'],
#             'client_name': data['client_name'],
#         }

#         # Save the OptyTracker model instance
#         opty_tracker = OptyTracker.objects.create(**opty_data)

#         # Set the many-to-many relations
#         opty_tracker.accelerators.set(accelerators)
#         opty_tracker.Competations.set(competations)
#         opty_tracker.Microservices.set(microservices)

#         serializer = OptyTrackerSerializer(opty_tracker)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_data = data.pop('accelerators', None)
#         competations_data = data.pop('competations', None)
#         microservices_data = data.pop('microservices', None)

#         # Split the provided data into separate lists
#         accelerators_list = [x.strip() for x in accelerators_data.split(',') if x.strip()]
#         competations_list = [x.strip() for x in competations_data.split(',') if x.strip()]
#         microservices_list = [x.strip() for x in microservices_data.split(',') if x.strip()]

#         # Create or retrieve the related models and update the data
#         accelerators = []
#         for accelerator_name in accelerators_list:
#             accelerator, _ = Accelerator.objects.get_or_create(acc_name=accelerator_name)
#             accelerators.append(accelerator)

#         competations = []
#         for competation_name in competations_list:
#             competation, _ = Competation.objects.get_or_create(name=competation_name)
#             competations.append(competation)

#         microservices = []
#         for microservice_name in microservices_list:
#             microservice, _ = Microservice.objects.get_or_create(name=microservice_name)
#             microservices.append(microservice)

#         # Check for existing values in the database
#         existing_accelerators = Accelerator.objects.filter(acc_name__in=accelerators_list)
#         existing_competations = Competation.objects.filter(name__in=competations_list)
#         existing_microservices = Microservice.objects.filter(name__in=microservices_list)

#         accelerators.extend(existing_accelerators)
#         competations.extend(existing_competations)
#         microservices.extend(existing_microservices)

#         opty_data = {field: data.get(field) for field in data.keys() if field != 'accelerators' and field != 'competations' and field != 'microservices'}

#         # Save the OptyTracker model instance
#         opty_tracker = OptyTracker.objects.create(**opty_data)

#         # Set the many-to-many relations
#         opty_tracker.accelerators.set(accelerators)
#         opty_tracker.Competations.set(competations)
#         opty_tracker.Microservices.set(microservices)

#         serializer = OptyTrackerSerializer(opty_tracker)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)





# from django.db import transaction

# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         with transaction.atomic():
#             accelerators = []
#             for name in accelerators_list:
#                 accelerator, _ = Accelerator.objects.get_or_create(acc_name=name)
#                 accelerators.append(accelerator)

#             competations = []
#             for name in competations_list:
#                 competation, _ = Competation.objects.get_or_create(name=name)
#                 competations.append(competation)

#             microservices = []
#             for name in microservices_list:
#                 microservice, _ = Microservice.objects.get_or_create(name=name)
#                 microservices.append(microservice)

#             # Save the OptyTracker model instance
#             opty_tracker = OptyTracker.objects.create(**data)

#             # Set the many-to-many relations
#             opty_tracker.accelerators.set(accelerators)
#             opty_tracker.Competations.set(competations)
#             opty_tracker.Microservices.set(microservices)

#             serializer = OptyTrackerSerializer(opty_tracker)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)




# from django.db import transaction

# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         with transaction.atomic(using='default'):
#             accelerators = []
#             for name in accelerators_list:
#                 with transaction.atomic(using='default'):
#                     accelerator, _ = Accelerator.objects.get_or_create(acc_name=name)
#                 accelerators.append(accelerator)

#             competations = []
#             for name in competations_list:
#                 with transaction.atomic(using='default'):
#                     competation, _ = Competation.objects.get_or_create(name=name)
#                 competations.append(competation)

#             microservices = []
#             for name in microservices_list:
#                 with transaction.atomic(using='default'):
#                     microservice, _ = Microservice.objects.get_or_create(name=name)
#                 microservices.append(microservice)

#             # Save the OptyTracker model instance
#             with transaction.atomic(using='default'):
#                 opty_tracker = OptyTracker.objects.create(**data)

#             # Set the many-to-many relations
#             opty_tracker.accelerators.set(accelerators)
#             opty_tracker.Competations.set(competations)
#             opty_tracker.Microservices.set(microservices)

#             serializer = OptyTrackerSerializer(opty_tracker)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)





# from django.db import transaction
# from django.db.utils import IntegrityError

# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         with transaction.atomic():
#             accelerators = []
#             for name in accelerators_list:
#                 try:
#                     accelerator, _ = Accelerator.objects.get_or_create(acc_name=name)
#                 except IntegrityError:
#                     accelerator = Accelerator.objects.get(acc_name=name)
#                 accelerators.append(accelerator)

#             competations = []
#             for name in competations_list:
#                 try:
#                     competation, _ = Competation.objects.get_or_create(name=name)
#                 except IntegrityError:
#                     competation = Competation.objects.get(name=name)
#                 competations.append(competation)

#             microservices = []
#             for name in microservices_list:
#                 try:
#                     microservice, _ = Microservice.objects.get_or_create(name=name)
#                 except IntegrityError:
#                     microservice = Microservice.objects.get(name=name)
#                 microservices.append(microservice)

#             # Save the OptyTracker model instance
#             opty_tracker = OptyTracker.objects.create(**data)

#             # Set the many-to-many relations
#             opty_tracker.accelerators.set(accelerators)
#             opty_tracker.Competations.set(competations)
#             opty_tracker.Microservices.set(microservices)

#             serializer = OptyTrackerSerializer(opty_tracker)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# from django.db import transaction
# from django.core.exceptions import MultipleObjectsReturned

# class OptyTrackerAPIView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract the related data from the request
#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         with transaction.atomic():
#             # Create or retrieve Accelerator objects
#             accelerators = []
#             for name in accelerators_list:
#                 try:
#                     accelerator = Accelerator.objects.get(acc_name=name)
#                 except MultipleObjectsReturned:
#                     accelerator = Accelerator.objects.filter(acc_name=name).first()
#                 except Accelerator.DoesNotExist:
#                     accelerator = Accelerator.objects.create(acc_name=name)
#                 accelerators.append(accelerator)

#             # Create or retrieve Competation objects
#             competations = []
#             for name in competations_list:
#                 try:
#                     competation = Competation.objects.get(name=name)
#                 except MultipleObjectsReturned:
#                     competation = Competation.objects.filter(name=name).first()
#                 except Competation.DoesNotExist:
#                     competation = Competation.objects.create(name=name)
#                 competations.append(competation)

#             # Create or retrieve Microservice objects
#             microservices = []
#             for name in microservices_list:
#                 try:
#                     microservice = Microservice.objects.get(name=name)
#                 except MultipleObjectsReturned:
#                     microservice = Microservice.objects.filter(name=name).first()
#                 except Microservice.DoesNotExist:
#                     microservice = Microservice.objects.create(name=name)
#                 microservices.append(microservice)

#             # Save the OptyTracker model instance
#             opty_tracker = OptyTracker.objects.create(**data)

#             # Set the many-to-many relations
#             opty_tracker.accelerators.set(accelerators)
#             opty_tracker.Competations.set(competations)
#             opty_tracker.Microservices.set(microservices)

#             serializer = OptyTrackerSerializer(opty_tracker)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)



from django.db import transaction
from django.core.exceptions import MultipleObjectsReturned

class OptyTrackerAPIViewPost(APIView):
    def post(self, request):
        data = request.data

        # Extract the related data from the request
        accelerators_list = data.pop('accelerators', [])
        competations_list = data.pop('competations', [])
        microservices_list = data.pop('microservices', [])

        with transaction.atomic():
            # Create or retrieve Accelerator objects
            accelerators = []
            accelerator_dict = {}
            for name in accelerators_list:
                try:
                    accelerator = accelerator_dict[name]
                except KeyError:
                    try:
                        accelerator = Accelerator.objects.get(acc_name=name)
                        accelerator_dict[name] = accelerator
                    except MultipleObjectsReturned:
                        accelerator = Accelerator.objects.filter(acc_name=name).first()
                        accelerator_dict[name] = accelerator
                    except Accelerator.DoesNotExist:
                        accelerator = Accelerator.objects.create(acc_name=name)
                        accelerator_dict[name] = accelerator
                accelerators.append(accelerator)

            # Create or retrieve Competation objects
            competations = []
            competation_dict = {}
            for name in competations_list:
                try:
                    competation = competation_dict[name]
                except KeyError:
                    try:
                        competation = Competation.objects.get(name=name)
                        competation_dict[name] = competation
                    except MultipleObjectsReturned:
                        competation = Competation.objects.filter(name=name).first()
                        competation_dict[name] = competation
                    except Competation.DoesNotExist:
                        competation = Competation.objects.create(name=name)
                        competation_dict[name] = competation
                competations.append(competation)

            # Create or retrieve Microservice objects
            microservices = []
            microservice_dict = {}
            for name in microservices_list:
                try:
                    microservice = microservice_dict[name]
                except KeyError:
                    try:
                        microservice = Microservice.objects.get(name=name)
                        microservice_dict[name] = microservice
                    except MultipleObjectsReturned:
                        microservice = Microservice.objects.filter(name=name).first()
                        microservice_dict[name] = microservice
                    except Microservice.DoesNotExist:
                        microservice = Microservice.objects.create(name=name)
                        microservice_dict[name] = microservice
                microservices.append(microservice)

            # Save the OptyTracker model instance
            opty_tracker = OptyTracker.objects.create(**data)

            # Set the many-to-many relations
            opty_tracker.accelerators.set(accelerators)
            opty_tracker.Competations.set(competations)
            opty_tracker.Microservices.set(microservices)

            serializer = OptyTrackerSerializer(opty_tracker)
            return Response(serializer.data, status=status.HTTP_201_CREATED)






#PATCH


from rest_framework.exceptions import NotFound, APIException

class OptyTrackerAPIView(APIView):
    def patch(self, request, pk):
        try:
            opty_tracker = OptyTracker.objects.get(pk=pk)
        except OptyTracker.DoesNotExist:
            raise NotFound()

        data = request.data

        # Extract the related data from the request
        accelerators_list = data.pop('accelerators', [])
        competations_list = data.pop('competations', [])
        microservices_list = data.pop('microservices', [])

        try:
            with transaction.atomic():
                # Create or retrieve Accelerator objects
                accelerators = []
                accelerator_dict = {}
                for name in accelerators_list:
                    try:
                        accelerator = accelerator_dict[name]
                    except KeyError:
                        try:
                            accelerator = Accelerator.objects.get(acc_name=name)
                            accelerator_dict[name] = accelerator
                        except MultipleObjectsReturned:
                            accelerator = Accelerator.objects.filter(acc_name=name).first()
                            accelerator_dict[name] = accelerator
                        except Accelerator.DoesNotExist:
                            accelerator = Accelerator.objects.create(acc_name=name)
                            accelerator_dict[name] = accelerator
                    accelerators.append(accelerator)

                # Create or retrieve Competation objects
                competations = []
                competation_dict = {}
                for name in competations_list:
                    try:
                        competation = competation_dict[name]
                    except KeyError:
                        try:
                            competation = Competation.objects.get(name=name)
                            competation_dict[name] = competation
                        except MultipleObjectsReturned:
                            competation = Competation.objects.filter(name=name).first()
                            competation_dict[name] = competation
                        except Competation.DoesNotExist:
                            competation = Competation.objects.create(name=name)
                            competation_dict[name] = competation
                    competations.append(competation)

                # Create or retrieve Microservice objects
                microservices = []
                microservice_dict = {}
                for name in microservices_list:
                    try:
                        microservice = microservice_dict[name]
                    except KeyError:
                        try:
                            microservice = Microservice.objects.get(name=name)
                            microservice_dict[name] = microservice
                        except MultipleObjectsReturned:
                            microservice = Microservice.objects.filter(name=name).first()
                            microservice_dict[name] = microservice
                        except Microservice.DoesNotExist:
                            microservice = Microservice.objects.create(name=name)
                            microservice_dict[name] = microservice
                    microservices.append(microservice)

                # Update the OptyTracker instance with the provided data (including other fields)
                for field, value in data.items():
                    setattr(opty_tracker, field, value)
                opty_tracker.save()

                # Set the many-to-many relations
                opty_tracker.accelerators.set(accelerators)
                opty_tracker.Competations.set(competations)
                opty_tracker.Microservices.set(microservices)

                serializer = OptyTrackerSerializer(opty_tracker)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except APIException as e:
            return Response({'message': str(e)}, status=e.status_code)

        except Exception as e:
            return Response({'message': 'An error occurred while processing the request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from modtest.models import OptyTracker, Accelerator, Competation, Microservice
# from modtest.serializers import OptyTrackerSerializer

# class OptyTrackerAPIView(APIView):
#     def patch(self, request, pk):
#         opty_tracker = get_object_or_404(OptyTracker, pk=pk)
#         data = request.data

#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         with transaction.atomic():
#             accelerators = self.get_or_create_related_objects(Accelerator, 'acc_name', accelerators_list)
#             competations = self.get_or_create_related_objects(Competation, 'name', competations_list)
#             microservices = self.get_or_create_related_objects(Microservice, 'name', microservices_list)

#             # Update the OptyTracker instance with the provided data (including other fields)
#             for field, value in data.items():
#                 setattr(opty_tracker, field, value)
#             opty_tracker.save()

#             # Set the many-to-many relations
#             opty_tracker.accelerators.set(accelerators)
#             opty_tracker.Competations.set(competations)
#             opty_tracker.Microservices.set(microservices)

#             serializer = OptyTrackerSerializer(opty_tracker)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def get_or_create_related_objects(self, model, field_name, names_list):
#         related_objects = []
#         related_objects_dict = {}
#         for name in names_list:
#             related_object = related_objects_dict.get(name)
#             if not related_object:
#                 related_object = model.objects.filter(**{field_name: name}).first()
#                 if not related_object:
#                     related_object = model.objects.create(**{field_name: name})
#                 related_objects_dict[name] = related_object
#             related_objects.append(related_object)
#         return related_objects




# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from modtest.models import OptyTracker, Accelerator, Competation, Microservice
# from modtest.serializers import OptyTrackerSerializer

# class OptyTrackerAPIView(APIView):
#     def patch(self, request, pk):
#         opty_tracker = get_object_or_404(OptyTracker, pk=pk)
#         data = request.data

#         accelerators_list = data.pop('accelerators', [])
#         competations_list = data.pop('competations', [])
#         microservices_list = data.pop('microservices', [])

#         accelerators = self.get_or_create_related_objects(Accelerator, 'acc_name', accelerators_list)
#         competations = self.get_or_create_related_objects(Competation, 'name', competations_list)
#         microservices = self.get_or_create_related_objects(Microservice, 'name', microservices_list)

#         # Update the OptyTracker instance with the provided data (including other fields)
#         for field, value in data.items():
#             setattr(opty_tracker, field, value)
#         opty_tracker.save()

#         # Set the many-to-many relations
#         opty_tracker.accelerators.set(accelerators)
#         opty_tracker.Competations.set(competations)
#         opty_tracker.Microservices.set(microservices)

#         serializer = OptyTrackerSerializer(opty_tracker)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def get_or_create_related_objects(self, model, field_name, names_list):
#         related_objects = []
#         for name in names_list:
#             related_object = model.objects.filter(**{field_name: name}).first()
#             if not related_object:
#                 related_object = model.objects.create(**{field_name: name})
#             related_objects.append(related_object)
#         return related_objects





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











from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from reportlab.lib.pagesizes import A4
import requests

def generate_pdf(request, pk):
    try:
        # Construct the URL with the ID
        url = f'http://localhost:8000/get_opportunity/{pk}/'

        # Fetch the data from the endpoint
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Load the template
            template = get_template('pdf_template.html')

            # Render the template with the data
            rendered_template = template.render(data)

            # Create a BytesIO buffer for the PDF
            pdf_buffer = BytesIO()

            # Convert HTML to PDF with A4 page size
            pisa_status = pisa.CreatePDF(
                rendered_template,
                dest=pdf_buffer,
                pagesize=A4
            )

            # Check if PDF creation was successful
            if pisa_status.err:
                return HttpResponse("Failed to generate PDF")

            # Set the PDF file headers
            pdf = HttpResponse(
                pdf_buffer.getvalue(),
                content_type='application/pdf'
            )
            pdf['Content-Disposition'] = 'attachment; filename="output.pdf"'

            return pdf

        else:
            return HttpResponse("Failed to fetch data from the endpoint")

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
    
    
    
    
    
    
    
    
    # PUT
    
class OpportunityTrackerUpdate(APIView):
    def put(self, request, pk):
        try:
            opty_tracker = OptyTracker.objects.get(pk=pk)
        except OptyTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data

        # Extract the related data from the request
        accelerators_data = data.pop('accelerators', None)
        competations_data = data.pop('competations', None)
        microservices_data = data.pop('microservices', None)

        # Split the provided data into separate lists
        accelerators_list = [x.strip() for x in accelerators_data.split(',') if x.strip()] if isinstance(accelerators_data, str) else accelerators_data
        competations_list = [x.strip() for x in competations_data.split(',') if x.strip()] if isinstance(competations_data, str) else competations_data
        microservices_list = [x.strip() for x in microservices_data.split(',') if x.strip()] if isinstance(microservices_data, str) else microservices_data

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

        # Update the fields of the OpportunityTracker instance based on the request data
        for field, value in data.items():
            if field != 'accelerators' and field != 'competations' and field != 'microservices':
                setattr(opty_tracker, field, value)

        # Save the OpportunityTracker model instance
        opty_tracker.save()

        # Set the many-to-many relations
        opty_tracker.accelerators.set(accelerators)
        opty_tracker.Competations.set(competations)
        opty_tracker.Microservices.set(microservices)

        serializer = OptyTrackerSerializer(opty_tracker)
        return Response(serializer.data, status=status.HTTP_200_OK)





#PATCH


 
from rest_framework.exceptions import NotFound, APIException

class OpportunityTrackerUpdate(APIView):
    def patch(self, request, pk):
        # Retrieve the existing OptyTracker object with the given primary key (pk)
        opty_tracker = get_object_or_404(OptyTracker, pk=pk)

        data = request.data

        # Extract the related data from the request
        accelerators_list = data.pop('accelerators', [])
        competations_list = data.pop('competations', [])
        microservices_list = data.pop('microservices', [])

        try:
            with transaction.atomic():
                # Create or retrieve Accelerator objects based on the provided names
                # Using a dictionary for fast lookup to avoid multiple queries
                accelerator_dict = {a.acc_name: a for a in Accelerator.objects.filter(acc_name__in=accelerators_list)}
                accelerators = []
                for name in accelerators_list:
                    # Check if the accelerator already exists in the dictionary
                    accelerator = accelerator_dict.get(name)
                    if accelerator is None:
                        # If not, create a new Accelerator object with the given name
                        accelerator = Accelerator.objects.create(acc_name=name)
                        # Add the newly created Accelerator object to the dictionary for future reference
                        accelerator_dict[name] = accelerator
                    # Append the accelerator to the list of accelerators
                    accelerators.append(accelerator)

                # Create or retrieve Competation objects based on the provided names
                # Using a dictionary for fast lookup to avoid multiple queries
                competation_dict = {c.name: c for c in Competation.objects.filter(name__in=competations_list)}
                competations = []
                for name in competations_list:
                    # Check if the competation already exists in the dictionary
                    competation = competation_dict.get(name)
                    if competation is None:
                        # If not, create a new Competation object with the given name
                        competation = Competation.objects.create(name=name)
                        # Add the newly created Competation object to the dictionary for future reference
                        competation_dict[name] = competation
                    # Append the competation to the list of competations
                    competations.append(competation)

                # Create or retrieve Microservice objects based on the provided names
                # Using a dictionary for fast lookup to avoid multiple queries
                microservice_dict = {m.name: m for m in Microservice.objects.filter(name__in=microservices_list)}
                microservices = []
                for name in microservices_list:
                    # Check if the microservice already exists in the dictionary
                    microservice = microservice_dict.get(name)
                    if microservice is None:
                        # If not, create a new Microservice object with the given name
                        microservice = Microservice.objects.create(name=name)
                        # Add the newly created Microservice object to the dictionary for future reference
                        microservice_dict[name] = microservice
                    # Append the microservice to the list of microservices
                    microservices.append(microservice)

                # Update the OptyTracker instance with the provided data (including other fields)
                for field, value in data.items():
                    setattr(opty_tracker, field, value)
                # Save the updated OptyTracker object
                opty_tracker.save()

                # Set the many-to-many relations for accelerators, competations, and microservices
                opty_tracker.accelerators.set(accelerators)
                opty_tracker.Competations.set(competations)
                opty_tracker.Microservices.set(microservices)

                # Serialize the updated OptyTracker object for the response
                serializer = OptyTrackerSerializer(opty_tracker)
                # Return the serialized data with a JSON response and 200 OK status
                return Response(serializer.data, status=status.HTTP_200_OK)

        except APIException as e:
            # Handle APIException and return an appropriate error response
            return Response({'message': str(e)}, status=e.status_code)
        except Exception as e:
            # Handle any other exceptions and return a JSON response with a 500 Internal Server Error status
            return Response({'message': 'An error occurred while processing the request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#DELETE
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from .models import OptyTracker

# class OpportunityTrackerDelete(APIView):
#     def delete(self, request, pk):
#         opty_tracker = get_object_or_404(OptyTracker, pk=pk)
#         opty_tracker.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from .models import OptyTracker

# class OpportunityTrackerDelete(APIView):
#     def delete(self, request, pk):
#         try:
#             opty_tracker = OptyTracker.objects.get(pk=pk)
#         except OptyTracker.DoesNotExist:
#             return Response({'message': 'OptyTracker not found.'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             with transaction.atomic():
#                 # Retrieve related many-to-many objects
#                 accelerators = opty_tracker.accelerators.all()
#                 competations = opty_tracker.Competations.all()
#                 microservices = opty_tracker.Microservices.all()

#                 # Remove the many-to-many relations
#                 opty_tracker.accelerators.clear()
#                 opty_tracker.Competations.clear()
#                 opty_tracker.Microservices.clear()

#                 # Delete the OptyTracker instance
#                 opty_tracker.delete()

#                 # Delete the related many-to-many objects
#                 accelerators.delete()
#                 competations.delete()
#                 microservices.delete()

#                 return Response("Data is deleted")

#         except Exception as e:
#             return Response({'message': 'An error occurred while processing the request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import OptyTracker
from .serializers import OptyTrackerSerializer

class OpportunityTrackerDelete(APIView):
    def delete(self, request, pk):
        try:
            opty_tracker = OptyTracker.objects.get(pk=pk)
        except OptyTracker.DoesNotExist:
            return Response({'message': 'OptyTracker not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            with transaction.atomic():
                # Retrieve related many-to-many objects
                accelerators = opty_tracker.accelerators.all()
                competations = opty_tracker.Competations.all()
                microservices = opty_tracker.Microservices.all()

                # Remove the many-to-many relations
                opty_tracker.accelerators.clear()
                opty_tracker.Competations.clear()
                opty_tracker.Microservices.clear()

                # Delete the related many-to-many objects
                for accelerator in accelerators:
                    accelerator.delete()
                for competation in competations:
                    competation.delete()
                for microservice in microservices:
                    microservice.delete()

                # Delete the OptyTracker instance
                opty_tracker.delete()

                return Response("Data is deleted", status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'message': 'An error occurred while processing the request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message" : "Hello world this message is not connected to any database"})