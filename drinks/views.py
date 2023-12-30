from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



def drink_list(request):

    #get all the drinks
    #serialize them
    #return json

    drinks=Drink.objects.all()
    serializer=DrinkSerializer(drinks,many=True)
    return JsonResponse({'drinks':serializer.data},safe=False)
    

    


# here we're returning nothing other than object we can remove safe =False