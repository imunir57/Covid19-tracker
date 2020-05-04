from django.shortcuts import render
from .models import Cases
# Create your views here.
def home(request):
    cases = Cases.objects.all()
    context = {'cases' : cases}
    return render(request, 'home.html', context)

def caseChart(request):
    date = []
    cases = []
    queryset = Cases.objects.all()
    for i in queryset:
        s = str(i.date)
        date.append(s)
        cases.append(i.new_cases)
     
    return render(request, 'chart.html', {'date': date, 'cases' : cases,})
