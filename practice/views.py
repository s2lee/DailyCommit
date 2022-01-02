from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randint, sample


class Hello(APIView):
    def get(self, request):
        return Response("Hello")


@api_view(["GET"])
def goodbye(request):
    return Response("Goodbye")


@api_view(["GET"])
def make_lotto_number(request):
    lotto_number = sample([i for i in range(1, 46)], 6)
    return Response(lotto_number)



