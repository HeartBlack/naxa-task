from rest_framework.serializers import Serializer,FileField,ModelSerializer,StringRelatedField,SerializerMethodField

from naxa.models import Location, Projectdetails, Sector


class FileUploadSerializer(Serializer):
    excel_upload = FileField()

    class Meta:
        fileds = ['excel_upload']
      

class ProjectDetailsSerializer(ModelSerializer):
    class Meta:
        model = Projectdetails
        fields= "__all__"
        depth = 2
   



class LocationSerializer(ModelSerializer):
    count= SerializerMethodField("_get_projects_count")
    total_budget= SerializerMethodField("_get_total_budget")
    municipality= StringRelatedField(many=False)
    class Meta:
        model= Location
        fields = ["id","municipality","count","total_budget"]
    def _get_projects_count(self,obj):
        return obj.total_project
        
    def _get_total_budget(self,obj):
        return obj.total_budget




class SectorSerializer(ModelSerializer):

    count= SerializerMethodField("_get_projects_count")
    budget= SerializerMethodField("_total_budget")

    class Meta:
        model = Sector
        fields = ["id","sector_name","count","budget",]

    def _get_projects_count(self,obj):
        return (obj.total_project)
    def _total_budget(self,obj):
        
        return (obj.total_budget)






