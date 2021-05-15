from rest_framework import serializers
from django.contrib.auth.models import User
from auto.models import Cars, Mototechnics, Manufacturer, SpecializedTechnique, Trucks, Category


class ManufacturerSerializer(serializers.Serializer):
    brand = serializers.CharField()
    model = serializers.CharField()

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('brand'):
            instance.brand = validated_data.get('brand', instance.brand)
        if validated_data.get('model'):
            instance.brand = validated_data.get('model', instance.model)

        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('category_name'):
            instance.brand = validated_data.get('category_name', instance.brand)

        instance.save()
        return instance


class CarsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Cars
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

        instance.save()
        return instance


class MototechnicsSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Mototechnics
        fields = '__all__'




class TrucksSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(write_only=False)
    category = CategorySerializer(write_only=False)

    class Meta:
        model = Trucks
        fields = '__all__'

    def create(self, validated_data):
        return Mototechnics.objects.create(**validated_data)

        instance.save()
        return instance


class SpecializedTechniqueSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = SpecializedTechnique
        fields = '__all__'

    def create(self, validated_data):
        return Mototechnics.objects.create(**validated_data)

        instance.save()
        return instance
