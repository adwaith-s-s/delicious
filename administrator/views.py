from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import os
import base64
from django.template import RequestContext, loader
from django.conf import settings
from product.models import *
from authentication.models import *
from django.core.mail import send_mail
from order.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Dashboard(TemplateView):
    template_name = "administrator/home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        
        context = {}
        return render(request, self.template_name, context)


class OrderManagement(TemplateView):
    template_name = "administrator/orders.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        order = Order.objects.all().order_by('-id')

        paginator = Paginator(order, 6)
        page = request.GET.get('page')

        try:
            order = paginator.page(page)
        except PageNotAnInteger:
            order = paginator.page(1)
        except EmptyPage:
            order = paginator.page(paginator.num_pages)

        context = {'order': order}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        print(request.POST['checkout'])
        order = Order.objects.get(checkout__txnid=request.POST['checkout'])
        order.status = request.POST['status']
        order.save()
        return redirect('/administrator/ordermanagement/')


class DeliveredOrders(TemplateView):
    template_name = "administrator/delivered.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        delivered = Order.objects.filter(status='Order Delivered').order_by('-id')

        paginator = Paginator(delivered, 6)
        page = request.GET.get('page')

        try:
            delivered = paginator.page(page)
        except PageNotAnInteger:
            delivered = paginator.page(1)
        except EmptyPage:
            delivered = paginator.page(paginator.num_pages)

        context = {'delivered': delivered}
        return render(request, self.template_name, context)


class Messages(TemplateView):
    template_name = "administrator/messages.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        message = Message.objects.all().order_by('-id')

        paginator = Paginator(message, 6)
        page = request.GET.get('page')

        try:
            message = paginator.page(page)
        except PageNotAnInteger:
            message = paginator.page(1)
        except EmptyPage:
            message = paginator.page(paginator.num_pages)

        context = {'message': message}
        return render(request, self.template_name, context)


class Requests(TemplateView):
    template_name = "administrator/requests.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        requests = Request.objects.all().order_by('-id')

        paginator = Paginator(requests, 6)
        page = request.GET.get('page')

        try:
            requests = paginator.page(page)
        except PageNotAnInteger:
            requests = paginator.page(1)
        except EmptyPage:
            requests = paginator.page(paginator.num_pages)

        context = {'requests': requests}
        return render(request, self.template_name, context)

