from rest_framework import serializers
from .models import Pledge, Project

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = Pledge
        fields = '__all__'  # Turns  to Json

class PledgeDetailSerializer(PledgeSerializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount',instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get('anonymous',instance.anonymous)
        instance.Project  = validated_data.get('Project ',instance.Project)
        instance.supporter = validated_data.get('supporter',instance.supporter)
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id') # gives serializer instructions how to handle user. Users aren't allowed to choose what value they set
    class Meta:
        model = Project
        fields = '__all__' # Turns  to Json

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True) #specifies a list of pledges under the project detail

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal',instance.goal)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        return instance
    
