"""
Views for organizations end points.
"""
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.http.response import JsonResponse

from skilredi_keyterms_app.models import Term
from skilredi_keyterms_app import serializers


class KeyTermView(GenericAPIView):
    """
    View for adding or removing a key term.
    """

    def get(self, *args, **kwargs):  # pylint: disable=unused-argument
        """
        Retieve information for a given key term for a given course.
        """

        params = self.request.query_params.dict()
        
        if 'key_name' not in params:
            return Response("key name is not specified", status=status.HTTP_400_BAD_REQUEST)
        
        else: 
            try: 
                term = Term.objects.get(key_name=params['key_name'])
                serializer = serializers.TermSerializer(term, many=False)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

            except:
                return Response("key term does not exist in database", status=status.HTTP_400_BAD_REQUEST)

    def post(self, *args, **kwargs):  # pylint: disable=unused-argument
        """
        Add key terms from a given course number.
        """
        params = self.request.data
        terms_list = params.get('terms_list')

        for term_data in terms_list:

            try:
                term = Term.objects.get(key_name=term_data['key_name'])
                # updates term if it already exists in database
                serializer = serializers.TermSerializer(term, term_data)

            except Term.DoesNotExist:
                serializer = serializers.TermSerializer(data=term_data)

            if serializer.is_valid():
                serializer.save()

        return Response("Successfully added key terms", status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):  # pylint: disable=unused-argument
        """
        Add key terms from a given course number.
        """

        params = self.request.data
        terms_list = params.get('terms_list')

        for term in terms_list:

            try:
                term = Term.objects.get(key_name=term['key_name'], course_number=term['course_number'])
                term.delete()
            except:
                return Response(term, status=status.HTTP_200_OK)
            
        return Response("Successfully removed a term!", status=status.HTTP_200_OK)


class CourseTermsListView(GenericAPIView):
    """
    View all key terms specific to a single course
    """

    def get(self, *args, **kwargs):  # pylint: disable=unused-argument
        """
        Retieve key terms from a given course.
        """

        params = self.request.query_params.dict()

        if 'course_number' not in params:
            return Response("course is not specified", status=status.HTTP_400_BAD_REQUEST)
        
        else:                         
            term_list = Term.objects.filter(course_number=params['course_number'])
            serializer = serializers.TermSerializer(term_list, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class GlossaryListView(GenericAPIView):
    """
    Not course specific. For global platform use.
    Returns all key terms with all supporting information.
    """

    def get(self, *args, **kwargs):
        """
        Return all terms for every course.
        """
        term_list = Term.objects.all()
        serializer = serializers.TermSerializer(term_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    