from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Hello(APIView):
    def get(self, request):
        return Response("Hello")


@api_view(["GET"])
def goodbye(request):
    return Response("Goodbye")
