from django.shortcuts import render
from django.views import View
from .models import CalendarEvent, targetEvent
from django.shortcuts import render, redirect

class AddView(View):
    def get(self, request, *args, **kwargs):
        data=targetEvent.objects.all()
        return render(request, 'cal/add.html', {'data' : data})
    
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        image=request.FILES.get('image')
        
        new_event = CalendarEvent.objects.create(
            title = title,
            description = description,
            image = image
        )
        
        return redirect('calendar')

class MemoView(View):
    def get(self, request, *args, **kwargs):
        data=CalendarEvent.objects.all()
        return render(request, 'cal/memo.html',{'data' : data})

class TargetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/target.html', {})

class StateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/state.html')

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        data=targetEvent.objects.all()
        return render(request, 'cal/calendar.html', {'data' : data})
    
class Target2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/target2.html', {})
    
    def post(self, request, *args, **kwargs):
        target = request.POST.get('target')
        subtitle = request.POST.get('subtitle')

        new_event = targetEvent.objects.create(
            target=target,
            subtitle=subtitle
        )
        return redirect('calendar')

def target2(request):
    return render(request, 'cal/target.html')