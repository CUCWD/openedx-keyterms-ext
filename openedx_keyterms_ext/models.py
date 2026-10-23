"""
Database models for openedx_keyterms_ext.
"""
import json

from django.core.exceptions import ValidationError
from django.db import models


class Lessons(models.Model):
    """
    TODO: Holds module and lesson information for key terms.

    """

    module_number = models.IntegerField(null=True, blank=True)
    lesson_number = models.IntegerField(null=True, blank=True)
    module_name = models.TextField(null=True, blank=True)
    lesson_name = models.TextField(null=True, blank=True)
    lms_link = models.TextField(null=True, blank=True)
    course_number = models.CharField(max_length=255, db_index=True, null=True)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<Lessons, ID: {}>'.format(self.id)
    

class Term(models.Model):
    """
    TODO: replace with a brief description of the model.

    """

    key_name = models.CharField(max_length=255, db_index=True, help_text="Key Term Name")
    course_number = models.CharField(max_length=255, db_index=True, null=True)
    # I don't think this needs to be ManyToMany.
    # I have not seen an instance where there is more than one definition for a term.
    definition = models.TextField(null=False)
    course_lessons = models.ManyToManyField(Lessons)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<Term, ID: {}>'.format(self.id)

    
class DefinitionOverrides(models.Model):
    """
    TODO: Allows for an alternate definition for a key term based on course run.

    """

    key_name = models.ForeignKey(Term, on_delete=models.CASCADE)
    course_run = models.CharField(max_length=255, db_index=True, null=True)
    definition = models.TextField(null=False)
