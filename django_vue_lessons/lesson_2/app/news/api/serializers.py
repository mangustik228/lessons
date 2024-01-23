from rest_framework import serializers
import news.models as M
from rest_framework import status
from collections import OrderedDict
from datetime import datetime
from django.utils.timesince import timesince


class JournalistSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(read_only=True, many=True)
    # articles = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name="article-detail",
    #     read_only=True
    # )

    class Meta:
        model = M.Journalist
        # fields = "__all__"
        exclude = ("id",)


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    my_custom_field = serializers.SerializerMethodField()
    author = JournalistSerializer()
    # author = serializers.StringRelatedField()

    class Meta:
        model = M.Article
        # fields = ("title", "description", "body", "word")
        # fields = "__all__"  # we want all the fields of our model
        exclude = ("id", "created_at")  # want to exlude
        # we want to choose a few fields

    def get_my_custom_field(self, obj: M.Article):
        return "hello world"

    def get_time_since_publication(self, object: M.Article):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate_title(self, value: str):
        if value.lower() == "hello world":
            raise serializers.ValidationError("Title cannot be 'hello world'")
        return value


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.CharField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data: dict):
#         return M.Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         print(f"[{type(validated_data)}] {validated_data}")
#         print(f"[{type(instance)}] {instance}")
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get(
#             "description", instance.description)
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get(
#             "publication_date", instance.publication_date)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate(self, data: OrderedDict):
#         '''check that description and title are differernt'''
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Title and Desciption must be different")
#         return data

#     def validate_title(self, value: str):
#         print(type(value))
#         if len(value) < 60:
#             raise serializers.ValidationError(
#                 "The title has to be at least 60 chars long.")
#         return value

#     def validate_active(self, value):
#         print(type(value))
#         return value

#     def validate_publication_date(self, value):
#         print(f"publication_date type: {type(value)}")
#         return value
