from django.urls import path
from .views import PessoaListCreateView, PessoaDetailView

urlpatterns = [
    path("pessoas/", PessoaListCreateView.as_view(), name="pessoa-list-create"),
    path("pessoas/<int:pk>/", PessoaDetailView.as_view(), name="pessoa-detail"),
]

