from rest_framework import serializers

from authentication.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    # ForgeignKey로 연결된 모델의 __str__ 메소드에서 정의한 string를 리턴
    author = serializers.StringRelatedField()
    class Meta:
        model = Journal
        fields = '__all__'
