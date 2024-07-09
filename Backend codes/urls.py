from django.urls import path
from .import views

urlpatterns=[
    path('',views.serial_communication,name="serial_communication"),
    path('predict_view',views.predict_water_supply,name="predict_view"),
    path('home',views.home,name="home"),
    path('api',views.api,name="api"),
    # path('esp8266_endpoint',views.esp8266_endpoint,name="esp8266_endpoint"),
    # path('esp82661',views.esp8266,name="esp8266"),
    path('main',views.machinelearning,name="machinelearning")
]