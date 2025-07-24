from rest_framework import serializers
from ..models import Aircraft, Flight


class DefaultEmptyMethodFieldMixin:
    """
    Mixin to provide default empty string for any missing get_* method used by SerializerMethodField.
    """

    def __getattr__(self, name):
        if name.startswith("get_"):
            return lambda obj: ""
        raise AttributeError(
            f"{self.__class__.__name__} object has no attribute {name}"
        )


class BaseAircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = []  # Extend in subclasses


class BaseFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = []  # Extend in subclasses
