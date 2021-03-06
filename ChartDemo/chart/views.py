import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line
from pyecharts import options as opts

from django.shortcuts import render

from . import models

class Chart():
	def __init__(self, Module):
		self.Module = Module
		self.index = 1000  # Set a big init value so it will run get_value_from_db() at beginning
		self.data_list = []

	def get_value_from_db(self):
		last_time = self.Module.objects.last().added_date
		values = self.Module.objects.filter(added_date=last_time)
		self.data_list = [i.value for i in values]

	def get_data(self, length):
		if self.index >= length:
			self.get_value_from_db()
			self.index = 0
		else:
			self.index += length // 5
		return self.data_list[self.index : self.index + length//5]
		
def response_as_json(data):
	json_str = json.dumps(data)
	response = HttpResponse(
		json_str,
		content_type="application/json",
	)
	response["Access-Control-Allow-Origin"] = "*"
	return response


def json_response(data, code=200):
	data = {
		"code": code,
		"msg": "success",
		"data": data,
	}
	return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
	data = {
		"code": code,
		"msg": error_string,
		"data": {}
	}
	data.update(kwargs)
	return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def current() -> Line:
	line = (
		Line()
		.add_xaxis(list(range(10)))
		.add_yaxis(series_name="A相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.add_yaxis(series_name="B相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.add_yaxis(series_name="C相电流", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="电流"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line

voltage_module = Chart(models.Voltage)
def voltage() -> Line:
	data = voltage_module.get_data(100)
	line = (
		Line()
		.add_xaxis(list(range(20)))
		.add_yaxis(series_name='', 
				   y_axis=data,
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="电压"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line

def temperature(title) -> Line:
	line = (
		Line()
		.add_xaxis(list(range(10)))
		.add_yaxis(series_name="", 
				   y_axis=[randrange(0, 100) for _ in range(10)],
				   is_smooth=True,)
		.set_global_opts(
			title_opts=opts.TitleOpts(title=title),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value")
		)
		.dump_options_with_quotes()
	)
	return line


class CurrentChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(current()))
	
class VoltageChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(voltage()))

class TemperatureFirstChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(temperature("前端绕组")))

class TemperatureSecondChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(temperature("后端绕组")))

class TemperatureThirdChart(APIView):
	def get(self, request, *args, **kwargs):
		return JsonResponse(json.loads(temperature("冷却水")))

cnt = 9


class ChartUpdateView(APIView):
	def get(self, request, *args, **kwargs):
		global cnt
		cnt = cnt + 1
		return JsonResponse({"name": cnt, "value": randrange(0, 100)})

class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		# return HttpResponse(content=open("./templates/index.html").read())
		return render(request, 'chart/index.html')

class CurrentView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/current.html')

class VoltageView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/voltage.html')

class TemperatureFirstView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/temperatureFirst.html')

class TemperatureSecondView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/temperatureSecond.html')

class TemperatureThirdView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, 'chart/temperatureThird.html')
