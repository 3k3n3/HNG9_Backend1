from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer

@api_view(['GET'])
def getProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


    # profile = {
    #     'slackUsername' : 'Maestro',
    #     'backend' : True,
    #     'age' : 28,
    #     'bio' : 'I have interests in backend development and database. Passionate about data driven solutions to real-world problems. Looking for opportunities to develop my skills and build a career in database and software development.',
    # }
    
    # return Response(profile)
