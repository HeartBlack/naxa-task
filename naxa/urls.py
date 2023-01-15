from django.urls import path,include
from . import views


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'answer1',views.upload_file,basename="upload")


urlpatterns = [
    path("",include(router.urls)),
    # path("answer2/",views.projectdetails.as_view(),),
    path("answer2/",views.ProjectFilter.as_view(),),
    path("answer3/",views.sectorbase.as_view(),),
    path("answer4/",views.LocationDetails.as_view(),),
]
