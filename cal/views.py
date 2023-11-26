from django.shortcuts import render
from django.views import View

class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/add.html')

class MemoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/memo.html')

class TargetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/target.html', {})

class StateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/state.html')

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/calendar.html', {})
    
class Target2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/target2.html', {})

def target2(request):
    return render(request, 'cal/target.html')