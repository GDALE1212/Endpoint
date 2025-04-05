from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404

from .models import Contacts
from .serializers import contact_serializer

class ContactViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = contact_serializer

    @action(detail=False, methods=['get'], url_path='(?P<category>[^/.]+)')
    def filter_by_category(self, request, category=None):
        contacts = Contacts.objects.filter(category__iexact=category)
        serializer = self.get_serializer(contacts, many=True)
        return Response(serializer.data)
