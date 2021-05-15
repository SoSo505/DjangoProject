from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.core.exceptions import EmptyResultSet
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_.models import UserProfile
from auto.models import Cars, Manufacturer, Category, Mototechnics, Trucks, SpecializedTechnique
from auto.serializers import CarsSerializer, CategorySerializer, ManufacturerSerializer, MototechnicsSerializer, \
    TrucksSerializer, SpecializedTechniqueSerializer


# Create your views here.
class MyAdvertisements(generics.ListCreateAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        try:
            advertisements = Cars.objects.all()
        except EmptyResultSet:
            raise Http404
        return advertisements


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cars.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        user = get_object_or_404(queryset, pk=pk)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create(self, request):
        category = Category.objects.create(category_name=request.data['category_name'])
        category.save()
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def destroy(self, requset, pk):
        instance = Category.objects.get(id=pk)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=False)
    def update(self, request, pk):
        category = Category.objects.get(id=pk)
        category.category_name = request.data['category_name']
        category.save()
        serializer = CategorySerializer(category)

        return Response(serializer.data)

    permission_classes = [AllowAny]


class ManufacturerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cars.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        user = get_object_or_404(queryset, pk=pk)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create(self, request):
        manufacturer = Manufacturer.objects.create(model=request.data['model'],
                                                   brand=request.data['brand'])
        manufacturer.save()
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    def destroy(self, requset, pk):
        instance = Manufacturer.objects.get(id=pk)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=False)
    def update(self, request, pk):
        manufacturer = Manufacturer.objects.get(id=pk)
        manufacturer.brand = request.data['brand']
        manufacturer.model = request.data['model']
        manufacturer.save()
        serializer = ManufacturerSerializer(manufacturer)

        return Response(serializer.data)

    permission_classes = [AllowAny]


class CarsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        user = get_object_or_404(queryset, pk=pk)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create(self, request):
        car_data = request.data
        category = Category.objects.create(category_name=car_data['category_name'])
        manufacturer = Manufacturer.objects.create(brand=car_data['brand'], model=car_data['model'])

        new_car = Cars.objects.create(body=car_data['body'], transmission=car_data['transmission'],
                                      steeringWheel=car_data['steeringWheel'], driveWheel=car_data['driveWheel'],
                                      numberofdoors=car_data['numberofdoors'],
                                      engineCapacity=car_data['engineCapacity'],
                                      vin=car_data['vin'], description=car_data['description'],
                                      date=car_data['date'], yearOfManufacture=car_data['yearOfManufacture'],
                                      city=car_data['city'], status=car_data['status'],
                                      typeOfEngine=car_data['typeOfEngine'],
                                      mileage=car_data['mileage'], color=car_data['color'], price=car_data['price'],
                                      category=category, manufacturer=manufacturer)
        new_car.save()
        serializer = CarsSerializer(new_car)
        return Response(serializer.data)

    def destroy(self, requset, pk):
        instance = Cars.objects.get(id=pk)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=False)
    def update(self, request, pk):
        car_data = request.data
        cars = Cars.objects.get(id=pk)

        cars.body = car_data['body'], cars.transmission = car_data['transmission']
        cars.steeringWheel = car_data['steeringWheel'], cars.driveWheel = car_data['driveWheel']
        cars.numberofdoors = car_data['numberofdoors'], cars.engineCapacity = car_data['engineCapacity']
        cars.vin = car_data['vin'], cars.description = car_data['description']
        cars.date = car_data['date'], cars.yearOfManufacture = car_data['yearofManufacture']
        cars.city = car_data['city'], cars.status = car_data['status']
        cars.typeOfEngine = car_data['typeOfEngine'], cars.mileage = car_data['mileage']
        cars.color = car_data['color'], cars.price = car_data['price']
        cars.imageBase = car_data['imagebase'], cars.image1 = car_data['image1']
        cars.image2 = car_data['image2']
        cars.save()
        serializer = ManufacturerSerializer(Cars)

        return Response(serializer.data)

    def select(self, request, pk=None):
        queryset = Cars.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CarsSerializer(user)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class CarBrandAdvertisements(generics.ListAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        try:
            advertisements = Cars.objects.all().filter(manufacturer__brand=self.kwargs.get('brand'))
        except EmptyResultSet:
            raise Http404
        queryset = []
        for advertisement in advertisements:
            queryset.append(advertisement)
        return queryset

    permission_classes = [AllowAny]


class CarBrandModelAdvertisements(generics.ListAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        try:
            advertisements = Cars.objects.all().filter(manufacturer__brand=self.kwargs.get('brand'),
                                                       manufacturer__model=self.kwargs.get('model'))
        except EmptyResultSet:
            raise Http404
        queryset = []
        for advertisement in advertisements:
            queryset.append(advertisement)
        return queryset

    permission_classes = [AllowAny]


class CarByYearViewSet(viewsets.ViewSet):
    def list(self, request, year):
        queryset = Cars.objects.all().filter(yearOfManufacture=year)
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class MototechnicsApiView(APIView):

    def get(self, request):
        moto = Mototechnics.objects.all()
        serializer = MototechnicsSerializer(moto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        moto = request.data
        category = Category.objects.create(category_name=moto['category_name'])
        manufacturer = Manufacturer.objects.create(brand=moto['brand'], model=moto['model'])

        new_moto = Mototechnics.objects.create(type=moto['type'],
                                               engineCapacity=moto['engineCapacity'],
                                               yearOfManufacture=moto['yearOfManufacture'],
                                               city=moto['city'], status=moto['status'],
                                               mileage=moto['mileage'], price=moto['price'],
                                               category=category, manufacturer=manufacturer)
        new_moto.save()
        serializer = MototechnicsSerializer(new_moto)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [AllowAny]


#
# class MototechnicsListApiView(generics.ListCreateAPIView):
#     serializer_class = MototechnicsSerializer
#
#     def get_queryset(self):
#         try:
#             advertisements = Mototechnics.objects.all()
#         except EmptyResultSet:
#             raise Http404
#         return advertisements


class MototechnicsByTypeViewSet(viewsets.ViewSet):
    def list(self, request, type):
        queryset = Mototechnics.objects.all().filter(type=type)
        serializer = MototechnicsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class MototechnicsByBrandViewSet(viewsets.ViewSet):
    def list(self, request, brand):
        queryset = Mototechnics.objects.all().filter(manufacturer__brand=brand)
        serializer = MototechnicsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class MototechnicsByBrandModelViewSet(viewsets.ViewSet):
    def list(self, request, brand, model):
        queryset = Mototechnics.objects.all().filter(manufacturer__brand=brand, manufacturer__model=model)
        serializer = MototechnicsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class MototechnicsDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return Mototechnics.objects.get(pk=pk)
        except Mototechnics.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        moto = self.get_object(pk)
        serializer = MototechnicsSerializer(moto)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        moto = self.get_object(pk)
        serializer = MototechnicsSerializer(moto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        moto = Mototechnics.object.get(pk=pk)
        moto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [AllowAny]


class SpecializedTechniqueApiView(APIView):

    def get(self, request):
        technique = SpecializedTechnique.objects.all()
        serializer = SpecializedTechniqueSerializer(technique, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        spec = request.data
        category = Category.objects.create(category_name=spec['category_name'])
        manufacturer = Manufacturer.objects.create(brand=spec['brand'], model=spec['model'])

        new_spec = SpecializedTechnique.objects.create(type=spec['type'], producing_country=spec['producing_country'],
                                                       typeOfEngine=spec['typeOfEngine'],
                                                       yearOfManufacture=spec['yearOfManufacture'],
                                                       city=spec['city'], status=spec['status'],
                                                       mileage=spec['mileage'], price=spec['price'],
                                                       category=category, manufacturer=manufacturer)
        new_spec.save()
        serializer = SpecializedTechniqueSerializer(new_spec)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [AllowAny]


class SpecializedTechniqueDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return SpecializedTechnique.objects.get(pk=pk)
        except SpecializedTechnique.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        technique = self.get_object(pk)
        serializer = SpecializedTechniqueSerializer(technique)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        technique = self.get_object(pk)
        serializer = SpecializedTechniqueSerializer(technique, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        technique = SpecializedTechnique.object.get(pk=pk)
        technique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [AllowAny]


class SpecializedTechniqueByTypeApiView(APIView):
    def get_object(self, type):
        try:
            return SpecializedTechnique.objects.get(type=type)
        except SpecializedTechnique.DoesNotExist:
            raise Http404

    def get(self, request, type, format=None):
        technique = self.get_object(type)
        serializer = SpecializedTechniqueSerializer(technique)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


class SpecializedTechniqueTypeViewSet(viewsets.ViewSet):
    def list(self, request, type):
        queryset = SpecializedTechnique.objects.all().filter(type=type)
        serializer = SpecializedTechniqueSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class SpecializedTechniqueByBrandApiView(APIView):
    def get_object(self, brand):
        try:
            return SpecializedTechnique.objects.get(manufacturer__brand=brand)
        except SpecializedTechnique.DoesNotExist:
            raise Http404

    def get(self, request, brand, format=None):
        technique = self.get_object(brand)
        serializer = SpecializedTechniqueSerializer(technique)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
# @permission_classes((AllowAny))
def trucks_list(request):
    if request.method == 'GET':
        trucks = Trucks.objects.all()
        serializer = TrucksSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        trucks = request.data
        category = Category.objects.create(category_name=trucks['category_name'])
        manufacturer = Manufacturer.objects.create(brand=trucks['brand'], model=trucks['model'])

        new_trucks = Trucks.objects.create(type=trucks['type'],
                                           engineCapacity=trucks['engineCapacity'],
                                           yearOfManufacture=trucks['yearOfManufacture'],
                                           city=trucks['city'], status=trucks['status'],
                                           typeOfEngine=trucks['typeOfEngine'],
                                           mileage=trucks['mileage'], price=trucks['price'],
                                           category=category, manufacturer=manufacturer)
        new_trucks.save()
        serializer = SpecializedTechniqueSerializer(new_trucks)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((AllowAny))
def truck_detail(request, pk):
    try:
        truck = Trucks.objects.get(id=pk)
    except truck.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = TrucksSerializer(truck)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrucksSerializer(truck, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrucksByTypeApiView1(APIView):
    def get_object(self, type):
        try:
            trucks = Trucks.objects.get(type=type)
        except SpecializedTechnique.DoesNotExist:
            raise Http404
        queryset = []
        for advertisement in trucks:
            queryset.append(advertisement)
        return queryset

    def get(self, request, type, format=None):
        technique = self.get_object(type)
        serializer = TrucksSerializer(technique)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)


class TrucksByTypeViewSet(viewsets.ViewSet):
    def list(self, request, type):
        queryset = Trucks.objects.all().filter(type=type)
        serializer = MototechnicsSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]


class TrucksByBrandApiView(APIView):
    def get_object(self, brand):
        try:
            return Trucks.objects.get(manufacturer__brand=brand)
        except SpecializedTechnique.DoesNotExist:
            raise Http404

    def get(self, request, brand, format=None):
        technique = self.get_object(brand)
        serializer = TrucksSerializer(technique)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
