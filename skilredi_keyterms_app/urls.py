"""
URLs for skilredi_keyterms_app.
"""
from django.urls import include, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

app_name = 'keyterms'
urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="skilredi_keyterms_app/base.html")),
    re_path(r'^v1/', include('skilredi_keyterms_app.v1.urls'))
]
