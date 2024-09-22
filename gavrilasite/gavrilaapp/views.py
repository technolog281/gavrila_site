from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import report_model
from django.http import HttpResponse


def index(request):
    return render(request, 'gavrilaapp/index.html')


def report(request):
    if request.method == "POST":
        to_db = report_model()
        to_db.work_time = request.POST.get("text", 0)
        to_db.vt184_t = request.POST.get("text-1", 0)
        to_db.vt184_f = request.POST.get("text-2", 0)
        to_db.vt044_1_t = request.POST.get("text-3", 0)
        to_db.vt044_2_t = request.POST.get("text-4", 0)
        to_db.vt044_1_f = request.POST.get("text-5", 0)
        to_db.vt044_2_f = request.POST.get("text-6", 0)
        to_db.fix105_1_t = request.POST.get("text-7", 0)
        to_db.fix105_2_t = request.POST.get("text-8", 0)
        to_db.fix105_1_f = request.POST.get("text-9", 0)
        to_db.top_t = request.POST.get("text-10", 0)
        to_db.top_f = request.POST.get("text-11", 0)
        to_db.g206_t = request.POST.get("text-12", 0)
        to_db.g206_f = request.POST.get("text-13", 0)
        to_db.fix105_2_f = request.POST.get("text-14", 0)
        to_db.save()
    return HttpResponse(status=200)


def stat(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'gavrilaapp/stat.html', context)
