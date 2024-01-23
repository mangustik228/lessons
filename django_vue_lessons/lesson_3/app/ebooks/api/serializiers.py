from rest_framework import serializers
import ebooks.models as M


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = M.Review
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = M.Ebook
        fields = "__all__"
