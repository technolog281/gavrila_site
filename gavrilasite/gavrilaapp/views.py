from django.shortcuts import render
from .models import report_model
from django.http import HttpResponseRedirect
import json


def main(request):
    return render(request, 'gavrilaapp/main.html')


def report(request):
    with open('gavrilaapp/price.json') as file:
        price_dict = json.load(file)
    if request.method == "POST":
        to_db = report_model()
        to_db.work_time = request.POST.get("text", 0)

        to_db.vt184_t = request.POST.get("text-1", 0)
        to_db.vt184_f = request.POST.get("text-2", 0)
        to_db.vt184_i = int(to_db.vt184_t) + int(to_db.vt184_f)
        to_db.vt184_p = int(to_db.vt184_i) * price_dict['work_price']['vtylka_184']

        to_db.vt044_1_t = request.POST.get("text-3", 0)
        to_db.vt044_1_f = request.POST.get("text-5", 0)
        to_db.vt044_1_i = int(to_db.vt044_1_t) + int(to_db.vt044_1_f)
        to_db.vt044_1_p = int(to_db.vt044_1_i) * price_dict['work_price']['vtylka_044-1']

        to_db.vt044_2_t = request.POST.get("text-4", 0)
        to_db.vt044_2_f = request.POST.get("text-6", 0)
        to_db.vt044_2_i = int(to_db.vt044_2_t) + int(to_db.vt044_2_f)
        to_db.vt044_2_p = int(to_db.vt044_2_i) * price_dict['work_price']['vtylka_044-2']

        to_db.fix105_1_t = request.POST.get("text-7", 0)
        to_db.fix105_1_f = request.POST.get("text-9", 0)
        to_db.fix105_1_i = int(to_db.fix105_1_t) + int(to_db.fix105_1_f)
        to_db.fix105_1_p = int(to_db.fix105_1_i) * price_dict['work_price']['fixator-1']

        to_db.fix105_2_t = request.POST.get("text-8", 0)
        to_db.fix105_2_f = request.POST.get("text-14", 0)
        to_db.fix105_2_i = int(to_db.fix105_2_t) + int(to_db.fix105_2_f)
        to_db.fix105_2_p = int(to_db.fix105_2_i) * price_dict['work_price']['fixator-2']

        to_db.top_1_t = request.POST.get("text-10", 0)
        to_db.top_1_f = request.POST.get("text-15", 0)
        to_db.top_1_i = int(to_db.top_1_t) + int(to_db.top_1_f)
        to_db.top_1_p = int(to_db.top_1_i) * price_dict['work_price']['golovka-1']

        to_db.top_2_t = request.POST.get("text-16", 0)
        to_db.top_2_f = request.POST.get("text-11", 0)
        to_db.top_2_i = int(to_db.top_2_t) + int(to_db.top_2_f)
        to_db.top_2_p = int(to_db.top_2_i) * price_dict['work_price']['golovka-2']

        to_db.g206_t = request.POST.get("text-12", 0)
        to_db.g206_f = request.POST.get("text-13", 0)
        to_db.g206_i = int(to_db.g206_t) + int(to_db.g206_f)
        to_db.g206_p = int(to_db.g206_i) * price_dict['work_price']['gaika']

        to_db.day_total_s = to_db.g206_p + to_db.top_2_p + to_db.top_1_p + to_db.fix105_2_p + to_db.fix105_1_p + \
                            to_db.vt044_2_p + to_db.vt044_1_p + to_db.vt184_p
        to_db.day_total_time = float(to_db.work_time) * 142.05
        to_db.day_total = to_db.day_total_s + to_db.day_total_time
        to_db.date = request.POST.get("date")
        to_db.tg_id = '777'
        to_db.name = 'Mellivora'
        to_db.save()
    return HttpResponseRedirect("/")


def stat(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'gavrilaapp/stat.html', context)
