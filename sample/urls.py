from django.urls import path
from sample.views import *

urlpatterns = [
    path("invoice/", InvoiceCreateView.as_view()),
    path("invoice/<int:pk>", InvoiceDetailView.as_view()),
    path("draft_to_signA/<str:name>/", change_draft_to_sign_A),
    path("signA_to_signB/<str:name>/", change_sign_A_to_sign_B),
    path("signB_to_signC/<str:name>/", change_sign_B_to_sign_C),
    path("signC_to_approval/<str:name>/", change_sign_C_to_approval),
    path("ABC_to_draft/<str:name>/", change_A_B_C_to_draft)
]
