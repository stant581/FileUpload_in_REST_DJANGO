from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):

  class Meta():
    model = File
    fields = ('category','ads','url1','file1','timestamp')





