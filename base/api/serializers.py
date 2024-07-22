from rest_framework.serializers import ModelSerializer
#Serializers are used to amke a json object out of python object

from base.models import Notes

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Notes
        fields='__all__'