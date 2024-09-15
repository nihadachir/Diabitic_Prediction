
from django.urls import path
from .views import home,prediction,results

urlpatterns = [
    path('', home, name='home'),
    path('prediction', prediction, name='prediction'),
    path('prediction/result', results,name='results'),




]