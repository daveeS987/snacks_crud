from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class SnackListView(ListView):
    template_name = "snacks/snack_list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snacks/snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snacks/snack_create.html"
    model = Snack
    fields = ["name", "description", "purchaser"]


class SnackUpdateView(UpdateView):
    template_name = "snacks/snack_update.html"
    model = Snack
    fields = ["name", "description", "purchaser"]


class SnackDeleteView(DeleteView):
    template_name = "snacks/snack_delete.html"
    model = Snack
