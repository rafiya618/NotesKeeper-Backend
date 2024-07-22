from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import NoteSerializer
from base.models import Notes
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims, username is going to be encrypted in the token
        token['username'] = user.username  

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

@api_view(['GET'])   #takes the list of http methods
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    
    try:
        user=request.user
        notes = Notes.objects.filter(user=user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(f"Error fetching notes: {e}")
        return Response(status=500, data={"error": "Internal Server Error"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNote(request):
    try:
        user = request.user
        data = request.data
        note = Notes.objects.create(user=user, body=data['body'])
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    except Exception as e:
        print(f"Error creating note: {e}")
        return Response(status=500, data={"error": "Internal Server Error"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateNote(request, pk):
    try:
        user = request.user
        note = Notes.objects.get(id=pk, user=user)
        data = request.data
        note.body = data['body']
        note.save()
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    except Notes.DoesNotExist:
        return Response(status=404, data={"error": "Note not found"})
    except Exception as e:
        print(f"Error updating note: {e}")
        return Response(status=500, data={"error": "Internal Server Error"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    try:
        user = request.user
        note = Notes.objects.get(id=pk, user=user)
        note.delete()
        return Response({"success": "Note deleted"})
    except Notes.DoesNotExist:
        return Response(status=404, data={"error": "Note not found"})
    except Exception as e:
        print(f"Error deleting note: {e}")
        return Response(status=500, data={"error": "Internal Server Error"})