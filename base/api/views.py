from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, NetworkSerializer
from base.models import Network


@api_view(['GET'])
def getRoutes(request:Request) -> Response:
    routes = [
        'GET /api',
        'CREATE /api/user/register',
        'POST /api/user/login', 
        'READ (only authented user) /api/user/all', 
        'READ /api/network/all', 
        'CREATE api/network/create', 
        'UPDATE /api/network/update/<str:id>',
        'DELETE /api/network/delete/<str:id>',
    ]
    return Response(routes)


class UserRegistrationView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the user
            user = User.objects.create_user(username=username, password=password)

            # Return the user details
            return Response({'username': user.username, 'password': password}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request: Request) -> Response:
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
      

# only authenticated users can access this view
class UserListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NetworkListView(generics.ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NetworkCreateView(APIView):
    def post(self, request: Request) -> Response:
        serializer = NetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_network(request: Request, id: str) -> Response:
    item = Network.objects.get(pk=id)
    data = NetworkSerializer(instance=item, data=request.data)
     
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['Delete'])
def NetworkDeletionView(request: Request, id: str) -> Response:
    item = Network.objects.get(pk=id)
    data = NetworkSerializer(instance=item, data=request.data)
    
    if data.is_valid():
        item.delete()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
