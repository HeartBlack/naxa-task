from django.db import models

# Create your models here.
class Province(models.Model):
    name_province = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name_province


class District(models.Model):
    name_district = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name_district

class Municipality(models.Model):
    name_municipality = models.CharField(max_length=255,unique=True)

    @property
    def total_project(self):
        proj= Projectdetails.objects.filter(location__municipality__name_municipality=self.name_municipality).count()
        return proj
    
    @property
    def total_budget(self):
       proj= Projectdetails.objects.filter(location__municipality__name_municipality=self.name_municipality)
       total_amount = 0.0
       for amt in proj:
       
        total_amount += float(amt.commitments)
        return total_amount
    def __str__(self):
        return self.name_municipality

        
class Location(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE,default="")
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)


    @property
    def total_project(self):
        proj= Projectdetails.objects.filter(location__municipality=self.municipality).count()
        return proj
    @property
    def total_budget(self):
       proj= Projectdetails.objects.filter(location__municipality=self.municipality)
       total_amount = 0.0
       for amt in proj:
        total_amount += float(amt.commitments)
       return total_amount

    def __str__(self) -> str:
        return self.province.name_province + self.district.name_district + self.municipality.name_municipality

class Agency(models.Model):
    doner_name = models.CharField(max_length=255,default="")
    type_of = models.CharField(max_length=255)
    implementing_patner = models.CharField(max_length=255)
    humanitarian = models.CharField(max_length=255)
    executing_agency = models.CharField(max_length=255,default="")
    def __str__(self):
        return self.doner_name
    
class Sector(models.Model):
    sector_name = models.CharField(max_length=255)
    sector_id = models.IntegerField()
    
    def __str__(self):
        return self.sector_name
    @property
    def total_project(self):
        total_proj = Projectdetails.objects.filter(sector__sector_name=self.sector_name).all().count()
        return total_proj

    @property
    def total_budget(self):
        obj = Projectdetails.objects.filter(sector__sector_name=self.sector_name)
        amt=0.0

        for o in obj:
            amt += float(o.commitments)
        return amt

class Projectdetails(models.Model):
    title= models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    agreement_date= models.DateField()
    date_of = models.DateField()
    commitments = models.FloatField(max_length=255)
    budget_type = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    doner = models.ForeignKey(Agency,on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE,related_name="sector")


    def __str__(self):
        return self.title

    