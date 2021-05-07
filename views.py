from django.shortcuts import render

# import python file
from . import function
from .function import bmi_cal

# home page


def home(request):
    return render(request, 'home.html')

# result page


def result(request):
    # 抓取前端輸入的參數
    weight = request.POST.get('weight')
    height = request.POST.get('height')

    # 丟進計算fumction中
    bmi = bmi_cal(height, weight)

    # 回傳輸出到前端頁面
    context = {'bmi': bmi}

    return render(request, 'result.html', context)
