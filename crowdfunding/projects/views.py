from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializer import PledgeDetailSerializer, ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsownerOrReadOnly, IsPledgeSupporter #import new permission


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request): #get projects
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    

    def post(self,request): #create new project
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
            serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
        )
    
class ProjectDetail(APIView):
    #retrieve, update or delete a project instance
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, # register with a view
        IsownerOrReadOnly
    ]

    def get_object(self,pk):
        try:
            return Project.objects.get(pk=pk)
        #try:
            #project = Project.objects.get(pk=pk)
            #self.check_object_permissions(self.request, project) # modify with get object method to include permissions check
            #return Project
        
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
        instance=project,
        data=request.data,
        partial=True
    )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, format=None):
        Project = self.get_object(pk)
        Project.delete()
        return Response(status=status.HTTP_200_OK)

    
    
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):    
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgeDetail(APIView):
    #retrieve, update or delete a project instance
    permission_classes = [IsPledgeSupporter]

    def get_object(self,pk):
        try:
            return Pledge.objects.get(pk=pk)
        #try:
            #pledge = pledge.objects.get(pk=pk)
            #self.check_object_permissions(self.request, pledge) # modify with get object method to include permissions check
            #return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
        instance=pledge,
        data=request.data,
        partial=True
    )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, format=None):
        pledge  = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_200_OK)
