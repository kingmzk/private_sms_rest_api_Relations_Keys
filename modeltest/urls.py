"""
URL configuration for modeltest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modtest.views import (
    AcceleratorViewSet,
    OptyTrackerViewSet,
    OptyAccViewSet,
    CompetationViewSet,
    OppCompetationViewSet,
    MicroserviceViewSet,
    OppMicroserviceViewSet,
    get_opportunity,
    OptyTrackerAPIView,
    generate_pdf,
    OpportunityTrackerUpdate,
    OpportunityTrackerDelete,
)
from django.urls import reverse_lazy
from django.urls import path



router = DefaultRouter()
router.register('accelerators', AcceleratorViewSet, basename='accelerator')
router.register('optytrackers', OptyTrackerViewSet, basename='optytracker')
router.register('optyaccs', OptyAccViewSet, basename='optyacc')
router.register('competations', CompetationViewSet, basename='competation')
router.register('oppcompetations', OppCompetationViewSet, basename='oppcompetation')
router.register('microservices', MicroserviceViewSet, basename='microservice')
router.register('oppmicroservices', OppMicroserviceViewSet, basename='oppmicroservice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accelerators/<int:pk>/update/', AcceleratorViewSet.as_view({'put': 'update'}), name='accelerator-update'),
    path('get_opportunity/<int:pk>/', get_opportunity, name='get_opportunity'),
    path('api/optytracker/', OptyTrackerAPIView.as_view()),
    path('generate-pdf/<int:pk>/', generate_pdf, name='generate_pdf'),
    path('pdf-link/', lambda request: HttpResponse(f'<a href="{reverse_lazy("generate_pdf")}">Generate PDF</a>'), name='pdf_link'),
    path('opportunity/<int:pk>/', OpportunityTrackerUpdate.as_view(), name='opportunity-update'),
    path('opportunity/<int:pk>/', OpportunityTrackerUpdate.as_view(), name='opportunity-update'),
    path('opportunity/<int:pk>/', OpportunityTrackerDelete.as_view(), name='opportunity-delete'),

 
]
