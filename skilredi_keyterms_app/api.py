import logging

from django.conf import settings

from . import data

# PRIVATE METHODS
def _get_course_number(course_key):

    return(data.fetch_course_number(course_key))


def _get_course_run(course_key):

    return(data.fetch_course_run(course_key))


# PUBLIC METHODS
def bulk_remove_keyterms(keyterm_data):

    return(data.bulk_delete_keyterms(keyterm_data))


def bulk_add_keyterms(keyterm_data):

    return(data.bulk_create_keyterms(keyterm_data))


def remove_keyterm(keyterm):

    return(data.delete_keyterm(keyterm))


def add_keyterm(keyterm):

    return(data.create_keyterm(keyterm))


def get_keyterm(term_name):

    return(data.fetch_keyterm(term_name))


def get_course_terms(course_key):

    course_number = _get_course_number(course_key)
    return(data.fetch_course_terms(course_number))


def add_definition_override(keyterm_data):
    
    return(data.create_definition_override(keyterm_data))


def remove_definition_override(keyterm_data, course_key):

    course_run = _get_course_run(course_key)
    return(data.delete_definition_override(keyterm_data, course_run))
