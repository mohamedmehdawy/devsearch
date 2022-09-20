from dataclasses import fields
from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile, Skill

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
class ProjectsSerializer(serializers.ModelSerializer):
    owner = ProfilesSerializer()
    tags = TagsSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    
    # methods
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return serializer.data
    class Meta:
        model = Project
        fields = "__all__"