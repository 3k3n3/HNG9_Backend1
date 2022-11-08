from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Profile, Operation
from .serializers import ProfileSerializer, OperationSerializer

# Task1
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

# Task2
@api_view(['POST'])
def calculate(request):
    context = {
        "slackUsername" : "maestro",
    }

    ADDITION = ['addition', 'add', 'sum', 'summation','plus']
    SUBRACTION = ['difference', 'subtraction', 'reduce', 'decrease', 'minus']
    MULTIPLICATION = ['times', 'multiply', 'product', 'multiplication']

    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        
        # add words in operation_type in lower case to list
        wordList = [x.lower() for x in serializer.data['operation_type'].split(' ')]
        
        # # logic for getting imput x, y varibales from operation_type input
        # xy_variables = []
        # for x in wordList:
        #     try:
        #         xy_variables.append(int(x))
        #     except:
        #         pass

        # x, y = xy_variables[0], xy_variables[1]
        # # print(x)
        # # print(y)

        # if serializer.data['x']:
        #     print(True)


        for x in wordList:
            if x in ADDITION:
                result = serializer.data['x'] + serializer.data['y']
                context['result'] = result
                context['operation_type'] = 'addition'
            
            elif x in SUBRACTION:
                result = serializer.data['x'] - serializer.data['y']
                context['result'] = result
                context['operation_type'] = 'subtraction'

            elif x in MULTIPLICATION:
                result = serializer.data['x'] * serializer.data['y']
                context['result'] = result
                context['operation_type'] = 'multiplication'

        # # Using model enum/choicefield
        # if serializer.data['operation_type'] == "addition":
        #     result = serializer.data['x'] + serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        # if serializer.data['operation_type'] == "multiplication":
        #     result = serializer.data['x'] * serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        # if serializer.data['operation_type'] == "subtraction":
        #     result = serializer.data['x'] - serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        return Response(context)
        # return Response(serializer.data)

    # If data is not valid
    else:
        print('Wahala!!')
        return Response(status=status.HTTP_404_NOT_FOUND)
