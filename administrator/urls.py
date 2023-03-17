from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', Dashboard.as_view(), name='dadhboard'),
	path('ordermanagement/', OrderManagement.as_view(), name='ordermanagement'),
	path('deliveredorders/', DeliveredOrders.as_view(), name='deliveredorders'),
	path('messages/', Messages.as_view(), name='messages'),
	path('requests/', Requests.as_view(), name='requests'),
]