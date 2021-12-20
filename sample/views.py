from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from sample.models import InvoiceTest
from sample.serializer import InvoiceTestSerializer


class InvoiceCreateView(generics.ListCreateAPIView):
    queryset = InvoiceTest.objects.all()
    serializer_class = InvoiceTestSerializer
    permission_classes = [IsAdminUser]


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceTest.objects.all()
    serializer_class = InvoiceTestSerializer


@api_view(['GET', 'PATCH'])
def change_draft_to_sign_A(self, name):
    obj = generics.get_object_or_404(InvoiceTest, name=name)
    obj.from_draft_to_sign_A()
    obj.save()
    return Response('Awaiting Sign A')


@api_view(['GET', 'PATCH'])
def change_sign_A_to_sign_B(self, name):
    obj = generics.get_object_or_404(InvoiceTest, name=name)
    obj.from_sign_A_to_sign_B()
    obj.save()
    return Response('Awaiting Sign B')


@api_view(['GET', 'PATCH'])
def change_sign_B_to_sign_C(self, name):
    obj = generics.get_object_or_404(InvoiceTest, name=name)
    obj.from_sign_B_to_sign_C()
    obj.save()
    return Response('Awaiting Sign C')


@api_view(['GET', 'PATCH'])
def change_sign_C_to_approval(self, name):
    obj = generics.get_object_or_404(InvoiceTest, name=name)
    obj.from_sign_C_to_approval()
    obj.save()
    return Response('Awaiting Approval')


@api_view(['GET', 'PATCH'])
def change_A_B_C_to_draft(self, name):
    obj = generics.get_object_or_404(InvoiceTest, name=name)
    obj.from_A_B_C_to_draft()
    obj.save()
    return Response('Rejected')
