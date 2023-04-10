from rest_framework import serializers
from .models import Details, Students

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['Stuid','Name','Age','Gender','Degree','Email','Address','image','Admin_id']       
        
             
class StudentsSerializer(serializers.ModelSerializer):
    Details = DetailsSerializer(read_only=True, many=True)
    
    class Meta:
        model = Students
        fields = ['Admin_id','College','Details']  