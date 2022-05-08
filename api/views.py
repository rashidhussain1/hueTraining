from rest_framework.response import Response
from rest_framework.decorators import api_view
from myApp.models import Project, User, Issue, Comment
from .serializers import UserSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

#view for user table for GET and POST method---------------------------------------------------------------

class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#view for Issue table for GET and POST method---------------------------------------------------------------

from django.core.mail import EmailMessage
from django.conf import settings

class IssueView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request):
        email = EmailMessage(
            'new issue added',
            'A new issue has been added',
            settings.EMAIL_HOST_USER,
            ['rashidhussain060998@gmail.com'],
        )
        email.fail_silently = False
        email.send()
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get_object(self, issueId):
        return Issue.objects.get(issueId=issueId)
    
    def put(self, request, issueId, format=None):
        issueObj = self.get_object(issueId)
        serializer = IssueSerializer(issueObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not valid data')

    def delete(self, request, issueId, format=None):
        issueObj = self.get_object(issueId)
        issueObj.delete()
        return Response('Issue Deleted')
    

#view for Project table for GET and POST method--------------------------------------------------------------------

class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get_object(self, projectId):
        return Project.objects.get(projectId=projectId)
    
    def put(self, request, projectId, format=None):
        projectObj = self.get_object(projectId)
        serializer = ProjectSerializer(projectObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not valid data')

    def delete(self, request, projectId, format=None):
        projectObj = self.get_object(projectId)
        projectObj.delete()
        return Response('Project Deleted')

    
# View for Comment table for GET and POST method--------------------------------------------------------------------

class CommentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Comment.objects.all()
        serializer = CommentSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
