from rest_framework.serializers import ModelSerializer
from vorkers.models import Vorkers



class VorkersSerializer(ModelSerializer):
   class Meta:
       model = Vorkers
       fields = '__all__'
