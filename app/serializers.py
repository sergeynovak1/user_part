from rest_framework import serializers


class AuthFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        # Perform additional validation if needed
        return data