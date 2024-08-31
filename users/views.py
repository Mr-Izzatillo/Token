from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer, RegisterSerializer, ResetPasswordSerializer, UserSerializer   
from .models import User
from django.shortcuts import get_object_or_404



class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        if '@gmail.com' in  username_or_email:
            user = User.objects.filter(email=username_or_email).first()
            print(user)
            if user is not None:
                login(request, user)
                return Response(
                     data={
                        'success': True,
                        'message': 'User successfully logged in',
                        'access':user.token()['access'],
                        'refresh_token':user.token()['refresh']
                        },
                )
        else:
            user = authenticate(username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return Response(
                     data={
                        'success': True,
                        'message': 'User successfully logged in',
                        'access':user.token()['access'],
                        'refresh_token':user.token()['refresh']
                        },
                )
            
            
        
class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        firstname = request.data.get('first_name')
        lastname = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
    
        if username and User.objects.filter(username=username).exists():
            return Response(
                data={ 
                    'success':True,
                    'massage': 'Username alredy registered',
                }
            )
            
        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        return Response(
            data={
               'success': True,
               'massage': 'Username successfully registred',
            }
        )
        

class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        user = request.user 
        print(user)
        if not user.check_password(old_password):
            return Response(
                data={
                    'success': False,
                    'message': 'Old password is incorrect',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if old_password == new_password:
            return Response(
                data={
                    'success': False,
                    'message': 'New password cannot be the same as the old password',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()
        return Response(
            data={
                'success': True,
                'message': 'Password successfully updated',
            },
            status=status.HTTP_200_OK
        )


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(instance=user, many = True)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=400)
    
class UserDetailView(APIView):
    def get(self, request, id):
        user =  User.objects.get(id=id)
        serializer = UserSerializer(instance=user)
        return Response(data=serializer.data)
    
    def put(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, id):
        user = User.objects.get(id=id)
        serializer= UserSerializer(data=request.data, instance=user, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(
            data={
                'massage': "User delete"
            }
        )
        
        
        