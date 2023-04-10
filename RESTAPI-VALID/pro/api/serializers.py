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
    
    def validate_College(self, value):
        if not value.isalpha():
             raise serializers.ValidationError( "Please enter alphabetical characters only !")
        return value 
        
    def validate_Admin_id(self, value):
        if value > 5:
            raise serializers.ValidationError('Admin_id allow only minimum five users only !')
        return value