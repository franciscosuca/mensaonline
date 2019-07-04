from testApp.models import Note

from testApp.serializers import NoteSerializer
from rest_framework import viewsets

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Uncomment the next block of code to use authentication
# from rest_framework.authentication import BasicAuthentication

# Uncomment the next block of code to bypass the authentication
from rest_framework.permissions import AllowAny
@permission_classes((AllowAny, ))

# Note viewset
# Create, edit or display our notes via the API

class NoteViewSet(viewsets.ModelViewSet):
    """
    Add comments here
    """
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all() #Select note
    serializer_class = NoteSerializer #Serelize data
