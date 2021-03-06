from rest_framework import serializers

from ..models import Event, Place, Testimony, TestimonyHipnoterapia


class PlaceSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')
    city = serializers.CharField(read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(many=False, read_only=True)

    class Meta:
        model = Event
        fields = ["id", "title", "subtitle", "place", "details", "open_for_subscriptions", "external_subscriptions", "iniciado", "finalizado"]


class TestimonySerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')
    customer = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Testimony
        fields = ["customer", "description", "image"]


class TestimonyHipnoterapiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonyHipnoterapia
        fields = ["id_video_youtube"]


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    message = serializers.CharField()

    def validate(self, data):
        if not data.get('email') and not data.get('phone'):
            raise serializers.ValidationError('Informe seu e-mail ou telefone!')
        return data
