from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from viewer.models import Notice, Category, Type, Condition


# Create your views here.

# Main page view only is_active=True
class NoticeList(ListView):
    model = Notice
    context_object_name = "notices"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notices"] = context["notices"].filter(is_active=True)
        context["count"] = context["notices"].count()
        context["categories"] = Category.objects.order_by('name').all()
        context["types"] = Type.objects.order_by('name').all()
        context["conditions"] = Condition.objects.order_by('name').all()

        search_input = self.request.GET.get("search") or ""
        category_input = self.request.GET.get("category") or ""
        type_input = self.request.GET.get("type") or ""
        condition_input = self.request.GET.get("condition") or ""

        if category_input:
            context["notices"] = context["notices"].filter(category=category_input)

        if type_input:
            context["notices"] = context["notices"].filter(type=type_input)

        if condition_input:
            context["notices"] = context["notices"].filter(condition=condition_input)

        if search_input:
            context["notices"] = context["notices"].filter(name__icontains=search_input)

        context["search_input"] = search_input
        return context


# Logged In User page only with users notices
class NoticeOwnList(LoginRequiredMixin, ListView):
    model = Notice
    context_object_name = "own_notices"
    template_name = "viewer/own_notice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["own_notices"] = context["own_notices"].filter(user=self.request.user)
        context["own_count"] = context["own_notices"].count()

        search_input = self.request.GET.get("search") or ""
        if search_input:
            context["own_notices"] = context["own_notices"].filter(name__icontains=search_input)

        context["search_input"] = search_input
        return context


# Details of published notice
class NoticeDetail(DetailView):
    model = Notice
    context_object_name = "notice"
    template_name = "viewer/notice.html"


# Creation of new notice
class NoticeCreate(LoginRequiredMixin, CreateView):
    model = Notice
    template_name = 'viewer/notice_add.html'
    fields = ["name", "description", "image", "price", "type", "category", "condition"]
    success_url = reverse_lazy("own_notices")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoticeCreate, self).form_valid(form)


# Updating of users notice
class NoticeUpdate(LoginRequiredMixin, UpdateView):
    model = Notice
    template_name = 'viewer/notice_update.html'
    fields = ["name", "description", "image", "price", "is_active", "type", "category", "condition"]
    success_url = reverse_lazy("own_notices")

    # Fix blocking logged user from accesing other users notice update option
    def get_object(self, queryset=None):
        notice = super(NoticeUpdate, self).get_object()
        if notice.user != self.request.user:
            raise Http404("Permission Denied")
        return notice


# Delete of notice prompt
class NoticeDelete(LoginRequiredMixin, DeleteView):
    model = Notice
    context_object_name = "notice"
    template_name = "viewer/notice_confirm_delete.html"
    success_url = reverse_lazy("own_notices")

    # Fix blocking logged user from accessing other users notice delete option
    def get_object(self, queryset=None):
        notice = super(NoticeDelete, self).get_object()
        if notice.user != self.request.user:
            raise Http404("Permission Denied")
        return notice
