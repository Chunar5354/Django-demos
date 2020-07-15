from django.urls import path
from . import views

urlpatterns = [
	path('currentChart/', views.CurrentChart.as_view(), name='chart'),
	path('voltageChart/', views.VoltageChart.as_view(), name='chart'),
	path('temperatureFirstChart/', views.TemperatureFirstChart.as_view(), name='chart'),
	path('temperatureSecondChart/', views.TemperatureSecondChart.as_view(), name='chart'),
	path('temperatureThirdChart/', views.TemperatureThirdChart.as_view(), name='chart'),
	path('lineUpdate/', views.ChartUpdateView.as_view(), name='chart'),
	path('', views.IndexView.as_view(), name='chart'),
	path('current/', views.CurrentView.as_view(), name='chart'),
	path('voltage/', views.VoltageView.as_view(), name='chart'),
	path('temperatureFirst/', views.TemperatureFirstView.as_view(), name='chart'),
	path('temperatureSecond/', views.TemperatureSecondView.as_view(), name='chart'),
	path('temperatureThird/', views.TemperatureThirdView.as_view(), name='chart'),
]

