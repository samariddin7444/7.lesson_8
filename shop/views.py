from django.views import View
from django.db.transaction import atomic
from django.shortcuts import render
from rest_framework.response import Response
from shop.models import Fruit,BestSell,Vegetable
from .serializers import FruitSerializer,VegetableSerializer,BestSellSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.decorators import action

class ShopPageView(View):
    def get(self, request):
        return render(request, 'shop.html')


class ShopDetailPageView(View):
    def get(self, request):
        return render(request, 'shop-detail.html')


class CartPageView(View):
    def get(self, request):
        return render(request, 'cart.html')


class ChackOutPageView(View):
    def get(self, request):
        return render(request, 'chackout.html')


class TestimonalPageView(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class NotFoundPageView(View):
    def get(self, request):
        return render(request, 'not-found.html')


class SearchResulPageView(View):
    def get(self, request):
        return render(request, 'search.html')


class ContactPageView:
    def get(self, request):
        return render(request, 'contact.html')

class FruitPageApiView(ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

  @action(detail=False, methods=['GET'])
    def euro(self, request, *args, **kwargs):
        fruits = self.get_queryset().filter(price_type='EURO').order_by('id')
        serializer = FruitSerializer(fruits, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def rating(self, request, *args, **kwargs):
        fruits = self.get_queryset().filter(rating=5).order_by('id')
        serializer = FruitSerializer(fruits, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def liked(self, request, *args, **kwargs):
        fruits = self.get_object()
        with atomic():
            fruits.likes += 1
            fruits.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        fruits = self.get_queryset()
        fruits = fruits.order_by('-likes')[:3]
        serializer = FruitSerializer(fruits, many=True)
        return Response(data=serializer.data)



class BestSellPageApiView(ModelViewSet):
    queryset = BestSell.objects.all()
    serializer_class = BestSellSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    @action(detail=False, methods=['GET'])
    def usd(self, request, *args, **kwargs):
        bestsells = self.get_queryset().filter(price_type='USD').order_by('id')
        serializer = BestSellSerializer(bestsells, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def rating(self, request, *args, **kwargs):
        bestsells = self.get_queryset().filter(rating=5).order_by('id')
        serializer = BestSellSerializer(bestsells, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def liked(self, request, *args, **kwargs):
        bestsells = self.get_object()
        with atomic():
            bestsells.likes += 1
            bestsells.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        bestsells = self.get_queryset()
        bestsells = bestsells.order_by('-likes')[:3]
        serializer = BestSellSerializer(bestsells, many=True)
        return Response(data=serializer.data)



class VegetablePageApiView(ModelViewSet):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    @action(detail=False, methods=['GET'])
    def euro(self, request, *args, **kwargs):
        vegetables = self.get_queryset().filter(price_type='EURO').order_by('id')
        serializer = VegetableSerializer(vegetables, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def rating(self, request, *args, **kwargs):
        vegetables = self.get_queryset().filter(rating=5).order_by('id')
        serializer = VegetableSerializer(vegetables, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def liked(self, request, *args, **kwargs):
        vegetables = self.get_object()
        with atomic():
            vegetables.likes += 1
            vegetables.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        vegetables = self.get_queryset()
        vegetables = vegetables.order_by('-likes')[:3]
        serializer = VegetableSerializer(vegetables, many=True)
        return Response(data=serializer.data)
