from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import LessonSerializer, ProductSerializer, AccessSerializer
from .models import Product, Lesson, Group, StudentInGroup


def index(request):
    return HttpResponse('Hello')


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    user_id = 1  ##Так же можно сделать что то наподобии user_id=User.objects.get(username='usernameexample'), тут уже от фантазии автора
    access_list = Product.objects.filter(accesslist=user_id)
    queryset = Lesson.objects.filter(product__in=access_list)


class AllProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RenderNewAccessAPIView(generics.CreateAPIView):
    serializer_class = AccessSerializer

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        user = request.user

        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Проверка, начался ли продукт
        if not product.date_started:

            # Если пользователя нет в группе - работаем
            if StudentInGroup.objects.filter(group_id__in=Group.objects.filter(product_name=product)).filter(student_id=user):
                return Response({'message': 'User already in group.'}, status=status.HTTP_400_BAD_REQUEST)

            # Распределение пользователей по группам
            groups = Group.objects.filter(product_name=product)
            for group in groups:
                if group.studentingroup_set.count() < product.max_users:
                    StudentInGroup.objects.create(group_id=group, student_id=user)
                    return Response({'message': 'User added to a group successfully'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'All groups are full for this product.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Product has already started.'}, status=status.HTTP_400_BAD_REQUEST)
