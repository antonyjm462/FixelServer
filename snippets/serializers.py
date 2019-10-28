from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.data = validated_data.get('code', instance.data)
        instance.save()
        return instance