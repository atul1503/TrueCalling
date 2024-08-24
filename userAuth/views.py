from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from userAuth.models import PhoneUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from caller.models import UserPhoneLabelMapping
from django.db.utils import IntegrityError


class RegisterView(APIView):
    '''
    post request to register the user and return token for the remaining api unrestricted usage
    accepts username,password and phonenumber as body param
    email is optional
    
    saves the registered user records in the caller model
    '''


    def post(self,request):
        try:
            username=request.data['username']
            email=request.data.get('email','')
            phonenumber=request.data['phonenumber']
        except KeyError:
            return Response({
                "message": 'username,password and phone number are mandatory.'
            },status=400)
        user=PhoneUser.objects.create_user(username=username,email=email,phonenumber=phonenumber)
        user.set_password(request.data.get("password",""))
        user.save()
        token=Token.objects.create(user=user)
        token.save()
        mapping=UserPhoneLabelMapping.objects.create(username=username,phonenumber=phonenumber)
        mapping.save()
        return Response({'token':token.key},status=200)


class RefreshView(APIView):
    '''
    post request to refresh the auth token for a registered user
    accepts username and password as body params
    return token
    '''


    def post(self,request):
        try:
            user=PhoneUser.objects.get(username=request.data.get("username",''))
            if user.check_password(request.data.get("password","")):
                Token.objects.filter(user=user).delete()
                token=Token.objects.create(user=user)
                token.save()
                return Response({
                    'token': token.key
                },status=200)
            else:
                return Response({
                    'message':'invalid password'

                },status=400)
        except:
            return Response({
                'message':'no such record'
            },status=404)