"""
URLS for organizations end points.
"""
from django.urls import re_path

from openedx_keyterms_ext.v1 import views

urlpatterns = [
    re_path(r'^course_terms/$', views.CourseTermsListView.as_view(), name='course_terms'),
    re_path(r'^glossary/$', views.GlossaryListView.as_view(), name='glossary'),
    re_path(r'^key_term/$', views.KeyTermView.as_view(), name="key_term"),
]
