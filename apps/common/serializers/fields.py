from rest_framework import serializers


class R2ImageField(serializers.ImageField):

    def to_representation(self, value):
        if not value:
            return None

        return str(value)