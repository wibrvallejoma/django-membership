from django.shortcuts import render, get_object_or_404, redirect
from plans.models import FitnessPlan


def home(request):
    plans = FitnessPlan.objects
    return render(request, 'plans/home.html', {'plans': plans})


def plan(request, pk):
    plan = get_object_or_404(FitnessPlan, pk=pk)
    if plan.premium:
        return redirect('join')
    else:
        return render(request, 'plans/plan.html', {'plan': plan})


def join(request):
    return render(request, 'plans/join.html')


def checkout(request):
    return render(request, 'plans/checkout.html')


def settings(request):
    return render(request, 'registration/settings.html')
