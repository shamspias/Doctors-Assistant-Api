from rest_framework import serializers

from . import models


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = [
            "diagnosis",
            "date_of_discharge",
            "phone",
            "date_of_admission",
            "age",
            "address",
            "prof_surgeon_consultant",
            "name",
            "sex",
        ]


class PatientInfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientInfos
        fields = '__all__'


class MediaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaImage
        fields = '__all__'


class MediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaVideo
        fields = '__all__'


class MediaDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaDocument
        fields = '__all__'


class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assign
        fields = '__all__'