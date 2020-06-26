from rest_framework import serializers
from .models import Website


class WebSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'link', 'description')
