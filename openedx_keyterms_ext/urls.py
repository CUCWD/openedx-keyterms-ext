"""
URLs for openedx_keyterms_ext.
"""
from django.urls import include, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

app_name = 'keyterms'
urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="openedx_keyterms_ext/base.html")),
    re_path(r'^v1/', include('openedx_keyterms_ext.v1.urls'))
]
