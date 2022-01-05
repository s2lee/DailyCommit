from django.shortcuts import get_object_or_404

from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        qs = Book.objects.all()
        serializer = BookSerializer(qs, many=True)  # 객체 목록 또는 쿼리셋을 serialize 할 때 , many=True 추가
        # many => queryset 에 대응. many 없으면 instance 1개가 올 것으로 기대하고 있어 에러 발생함.
        return Response(serializer.data)  # 클라이언트가 요청한 형태로 콘텐트를 렌더링함
        # Response -> Http or Json 요청 콘텐트에 맞게 자동으로 렌더링
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        #  장고와 달리 DRF 에서는 request 에서 데이터를 받을 때(request.data)
        #  반드시 .is_valid() 여부를 체크해야 한다.
        #  valid 하지 않을 때는 serializer.errors 를 리턴한다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 작성, 서버가 요청 접수 후 새 리소스를 작성함
        return Response(serializer.errors, status=400)  # 잘못된 요청


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    # 404 error 는 서버에서 요청한 리소스를 찾을 수 없을 때
    book = get_object_or_404(Book, pk=pk)  # 단일 객체에서 get_object_or_404() 이용하기
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        # request 에서 data 를 받았으니 .is_valid() 필수
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #  numeric HTTP status codes 보다 더 명확히 표현하고 싶을 때 status code 사용
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# APIView 목록, 생성
class BookListAPIView(APIView):
    def get(self, request):
        serializer = BookSerializer(Book.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# APIView 상세, 수정, 삭제
class BookDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BookSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = BookSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Mixins 상속 목록, 생성
class BookListMixins(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


# Mixins 상속 상세, 수정, 삭제
class BookDetailMixins(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Generic 목록, 생성
class BookListGenericAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Generic 상세, 수정, 삭제
class BookDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ViewSet 목록, 생성, 상세, 수정, 삭제
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
