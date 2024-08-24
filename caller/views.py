from rest_framework.views import APIView
from .serializers import UserPhoneLabelMappingSerializer
from .models import UserPhoneLabelMapping
from rest_framework.response import Response
from itertools import chain
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from userAuth.models import PhoneUser



class ReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        '''
            post request , reports the phone number with the provided label type
            for eg, it will label any present phonenumber to the label provided in request 
        '''
        serializer=UserPhoneLabelMappingSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            if UserPhoneLabelMapping.objects.filter(phonenumber=serializer.validated_data['phonenumber'],label=serializer.validated_data['label']).exists():
                return Response({
                    'message': 'Number already reported as '+serializer.validated_data['label'],
                },status=200)
            else:
                try: 
                    mapping=UserPhoneLabelMapping.objects.filter(phonenumber=serializer.validated_data['phonenumber'])
                    mapping.update(label="SPAM")
                    return Response(
                        {
                            "message": "phone number is reported."
                        },status=200
                    )
                except UserPhoneLabelMapping.DoesNotExist:
                    serializer.save()
        else:
            return Response(
                {
                    'message': 'bad request',
                    'error': serializer.errors
                },status=400
            )


class SearchByName(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        '''

        get request to search records by name.
        supports contains and startswith features, showing first the startswith records and then contains records.
        expects fullname in the request parameter.


        '''
        serializer=UserPhoneLabelMappingSerializer(data={'fullname':request.query_params.get('fullname')},partial=True)
        if not serializer.is_valid():
            return Response({
                'message': 'bad request'
            },status=400)
        starswith=UserPhoneLabelMapping.objects.filter(fullname__startswith=serializer.validated_data['fullname'])
        contains=UserPhoneLabelMapping.objects.filter(Q(fullname__contains=serializer.validated_data['fullname'])& ~Q(fullname__startswith=serializer.validated_data['fullname']))

        combined_results=list(chain(starswith,contains))
        combined_results=UserPhoneLabelMappingSerializer(combined_results,many=True)
        return Response(
            { 'results': combined_results.data}
            )


class SearchByPhone(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        '''
        
        get request to search by phone number. If in case, phone number is more reliable than name.
        expects phonenumber as query param. 

        
        '''
        serializer=UserPhoneLabelMappingSerializer(data={"phonenumber":request.query_params.get("phonenumber","")},partial=True)
        if not serializer.is_valid():
            return Response({
                'message': 'bad request',
                'error': serializer.errors
            },status=400)
        if PhoneUser.objects.filter(phonenumber=request.query_params.get("phonenumber")).exists():
            return Response({
              'result' :  UserPhoneLabelMappingSerializer(UserPhoneLabelMapping.objects.filter(phonenumber=serializer.validated_data['phonenumber'],username__isnull=False),many=True).data
            },status=200)
        else:
            return Response( {
            'result' : UserPhoneLabelMappingSerializer(UserPhoneLabelMapping.objects.filter(phonenumber=serializer.validated_data['phonenumber']),many=True).data
            },status=200)
    
class Generate(APIView):

    def get(self,request,*args,**kwargs):

        '''
        
        random endpoint to add data for testing
        
        '''

        UserPhoneLabelMapping.objects.create(fullname="Atul Tripathi",username="atultrip555", phonenumber="12345678910", label="VERIFIED")
        UserPhoneLabelMapping.objects.create(fullname="John Doe", username="john_doe1", phonenumber="1234567891", label="VERIFIED")
        UserPhoneLabelMapping.objects.create(fullname="Bharat Atul Aryan John", username="bharat_atul_aryan", phonenumber="1234567896", label="SPAM")
        return Response(status=200)