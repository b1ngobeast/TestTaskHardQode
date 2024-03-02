from rest_framework import serializers
from .models import Lesson, Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['product', 'name', 'link']


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'lesson_count']

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(product=obj).count()


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id']
