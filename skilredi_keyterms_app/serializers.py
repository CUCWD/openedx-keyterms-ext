"""
Serializers for key terms API.
"""

import json
import logging
from typing import SupportsRound

from rest_framework import serializers

from . import models

log = logging.getLogger(__name__)

def check_lesson_data(lesson_data):
    """
    Check if lesson data already exists.
    IF already exists, update entry if necessary
    If doesn't exist, create entry in database
    returns lesson object
    """

    try:
        lesson = models.Lessons.objects.filter(course_number=lesson_data['course_number']).filter(module_number=lesson_data['module_number']).get(lesson_number=lesson_data['lesson_number'])

        # If lesson information already exists, update it if necessary
        serializer = LessonSerializer.update(lesson, lesson_data)

    except models.Lessons.DoesNotExist:
        serializer = LessonSerializer(data=lesson_data)

        lesson = models.Lessons.objects.create(**lesson_data)

    return(lesson)


class LessonSerializer(serializers.ModelSerializer):
    """
    Gets lesson data ready to transport.
    """

    class Meta(object):
        model = models.Lessons
        fields = ['module_number', 'lesson_number', 'module_name', 'lesson_name', 'lms_link', 'course_number']

    def update(instance, validated_data):
        """
        Updates existing key term data into the database.
        """

        instance.module_name = validated_data.get('module_name', instance.module_name)
        instance.lesson_name = validated_data.get('lesson_name', instance.lesson_name)
        instance.lms_link = validated_data.get('lms_link', instance.lms_link)
        instance.save()


class TermSerializer(serializers.ModelSerializer):
    """
    Gets term data ready to transport.
    """

    definition = serializers.CharField()
    course_number = serializers.CharField(max_length=255)
    course_lessons = LessonSerializer(many=True)

    class Meta(object):

        model = models.Term
        fields = ['key_name', 'course_number', 'definition', 'course_lessons']

    def create(self, validated_data):
        """
        Saves key term data into the database.
        """

        course_number_data = validated_data.pop('course_number')
        definition_data = validated_data.pop('definition')
        course_lesson_data = validated_data.pop('course_lessons')
        key_name_data = validated_data.pop('key_name')

        term = models.Term.objects.create(key_name=key_name_data, definition=definition_data, course_number=course_number_data)
        term.save()

        for lesson in course_lesson_data:

            validated_lesson = check_lesson_data(lesson)
            term.course_lessons.add(validated_lesson)

        return term
    
    def update(self, instance, validated_data):
        """
        Updates existing key term data into the database.
        """
        course_lesson_data = validated_data.get('course_lessons')

        instance.definition = validated_data.get('definition', instance.definition)
        instance.save()

        for lesson in course_lesson_data:
            validated_lesson = check_lesson_data(lesson)
            instance.course_lessons.add(validated_lesson)

        return instance
    