from rest_framework import serializers
from .models import ToDoItem
from django.contrib.auth.models import User


class ToDoItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    content = serializers.CharField(required=True, allow_blank=False, max_length=100)
    isFinished = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        create an item
        """
        print validated_data
        return ToDoItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update an item
        """
        instance.content = validated_data.get('content', instance.content)
        instance.isFinished = validated_data.get('isFinished', instance.isFinished)
        instance.save()
        return instance

    class Meta:
        model = ToDoItem
        fields = ('id', 'owner', 'content', 'isFinished', 'created')


class ToDoUserSerializer(serializers.ModelSerializer):
    toDoItems = serializers.PrimaryKeyRelatedField(many=True, queryset=ToDoItem.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'toDoItems')

