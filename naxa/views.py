
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import  FileUploadSerializer,LocationSerializer,ProjectDetailsSerializer, SectorSerializer
import pandas as pd
from .models import Agency, District, Location, Municipality, Projectdetails, Province, Sector
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class upload_file(ViewSet):
    serializer_class  = FileUploadSerializer
    
    def list(self,request,format="application/vnd.ms-excel"):
        return Response("GET API")
    
    def create(self,request,format="application/vnd.ms-excel"):
        file_upload = request.FILES.get("excel_upload")

        content_type = file_upload.content_type
        print(content_type)

        if content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(file_upload,index_col=None,sheet_name="Sheet1")
            data_index = df.columns.get_loc("Province")
            for row in df.values:
                province_qr,status = Province.objects.get_or_create(name_province=row[data_index])
                district_qr,status = District.objects.get_or_create(name_district=row[data_index+1])
                municipality_qr,status = Municipality.objects.get_or_create(name_municipality=row[data_index+2])
          
                location_qr,status= Location.objects.get_or_create(province=province_qr,district=district_qr,municipality=municipality_qr)
                agency_qr,status = Agency.objects.get_or_create(doner_name=row[data_index+5],type_of=row[data_index+9],implementing_patner=row[data_index+7],humanitarian=row[data_index+11],executing_agency=row[data_index+6])


                sector_qr ,status = Sector.objects.get_or_create(sector_name=row[data_index+12],sector_id=row[data_index+13])

                project_qr ,status = Projectdetails.objects.update_or_create(title=row[data_index+3],status= row[data_index+4], agreement_date=row[data_index+15],date_of=row[data_index+16],
                commitments=row[data_index+14],budget_type=row[data_index+10],location=location_qr,doner=agency_qr,sector=sector_qr
            
            )
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)

        else:
            response= "Please make sure that the file is excel"
            return Response(response)


class projectdetails(ListAPIView):
    queryset = Projectdetails.objects.all()
    serializer_class = ProjectDetailsSerializer
    

class ProjectFilter(ListAPIView):
    queryset = Projectdetails.objects.all()
    serializer_class = ProjectDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title","sector","status",'date_of','agreement_date']

class LocationDetails(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["district","province"]



class sectorbase(ListAPIView):
    queryset= Sector.objects.all()
    serializer_class = SectorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sector_name"]


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        obj = Projectdetails.objects.all()
        abc =set()
        d = request.GET.get("district","")
        t = request.GET.get("title","")
        s = request.GET.get("status","")
        dt = request.GET.get("date_of","")
        ag = request.GET.get("agreement_date","")
        if d is not None and d is not "":
            l = Location.objects.filter(district__name_district=d)
            r = obj.filter(location__in=l)
            for a in r:
                abc.add(a.sector.sector_name)
            q = queryset.filter(sector_name__in=list(abc))

            serializer = self.get_serializer(q, many=True)
            response_list = serializer.data

        if t is not None and t is not "":
            i = obj.filter(title=t)
            for c in i:
                abc.add(c.sector.sector_id)
            q = queryset.filter(sector_id__in=list(abc))
            serializer = self.get_serializer(q, many=True)
            response_list = serializer.data


        if dt is not None and dt is not "":
            try:
                i = obj.filter(date_of=dt)
                for c in i:
                    print(c.sector)
                    abc.add(c.sector.sector_id)
                q = queryset.filter(sector_id__in=list(abc))
                serializer = self.get_serializer(q, many=True)
                response_list = serializer.data
            except:
                response_list = ["Date Format must be in YYYY-MM-DD"]

        if ag is not None and ag is not "":
            try:
                i = obj.filter(agreement_date=ag)
                for c in i:
                    abc.add(c.sector.sector_id)
                q = queryset.filter(sector_id__in=list(abc))
                serializer = self.get_serializer(q, many=True)
                response_list = serializer.data
            except:
                response_list = ["Date Format must be in YYYY-MM-DD"]

        if s is not None and s is not "":
            i = obj.filter(status=s)
            for c in i:
                print(c.sector)
                abc.add(c.sector.sector_id)
            q = queryset.filter(sector_id__in=list(abc))
            serializer = self.get_serializer(q, many=True)
            response_list = serializer.data


        if len(response_list) >= 1 :
            total_project = obj.count()
            total_amt= 0.0
            for t in obj:
                total_amt += float(t.commitments)     
            response_list.insert(0,{"summery":{"Total Project":total_project,"Total Amount":total_amt}})
            return Response(response_list)
        else:
            return Response([])