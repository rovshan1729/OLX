from rest_framework import serializers
from . import models

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )

class PostSerializer(serializers.ModelSerializer):
    category = MainPageSerializer()

    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'description',
            'price_type',
            'currency',
            'price',
            'status',
            'views',
            'private_or_business_figure',
            'condition',
            'is_active',
            'auto_renewal',
            'location',
            'user',
            'contact_person_name',
            'email',
            'phone_number',
        )
    