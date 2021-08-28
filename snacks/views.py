from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class SnackListView(ListView):
    pass


class SnackDetailView(DetailView):
    pass


class SnackCreateView(CreateView):
    pass


class SnackUpdateView(UpdateView):
    pass


class SnackDeleteView(DeleteView):
    pass
