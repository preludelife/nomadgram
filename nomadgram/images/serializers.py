from rest_framework import serializers
from taggit_serializer.serializers import(TagListSerializerField, TaggitSerializer)
from . import models
from nomadgram.users import models as user_models



class SmallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'
        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        #fields = '__all__'
        fields = (
            'id',
            'message',
            'creator',
        )


class LikeSerializer(serializers.ModelSerializer):    

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    #likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            #'likes',
            'like_count',
            'creator',
            'tags',
            'created_at',
            #'tags',
           # 'natural_time',
           # 'is_liked',
           # 'is_vertical'
        )


class InputImageSerializer(serializers.ModelSerializer):

    #file = serializers.FileField(required=False)

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )
