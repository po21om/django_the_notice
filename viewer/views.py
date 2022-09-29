from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView


# Create your views here.


class NoticeList(ListView):
    pass


class NoticeOwnList(LoginRequiredMixin, NoticeList):
    pass


class NoticeDetail(DetailView):
    pass


class NoticeCreate(LoginRequiredMixin, CreateView):
    pass


class NoticeUpdate(LoginRequiredMixin, UpdateView):
    pass


class NoticeDelete(LoginRequiredMixin, DetailView):
    pass

