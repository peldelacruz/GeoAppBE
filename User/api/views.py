from django.contrib.auth.models import User
from ..models import CustomUser, Company, Project
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from User.api.serializers import ProjectSerializer
import jwt

class TokenValidate(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {"content": "This view is protected"}
        return Response(content)

@api_view(['GET'])  
def getRoutes(request): 
    routes = [ 
        '/api/token',
        '/api/token/refresh/',
    ]
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, ])
def authenticate_user(request, token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return Response(decoded)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def ApiUserRegister(request, company, username):
    try:
        company_id = Company.objects.get(company=company)
        username_id = User.objects.get(username=username)
        if CustomUser.objects.filter(company_id=company_id, username_id=username_id).exists():
            response = dict(company=company, username=username, message="The user is registered in the company", status=status.HTTP_302_FOUND, success=True, validate="company-validation")
    except:
        if not Company.objects.filter(company=company).exists():
            response = dict(company=company, username=username, message="The company is not registered", status=status.HTTP_404_NOT_FOUND, success=False, validate="company-validation")
        else:    
            response = dict(company=company, username=username, message="The user is not registered.", status=status.HTTP_404_NOT_FOUND, success=True, validate="company-validation")
    return JsonResponse(response)

@api_view(['GET', 'POST'])
def project_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        customusers = CustomUser.objects.all()
        serializer = ProjectSerializer(customusers, many=True)
        return Response(serializer.data)