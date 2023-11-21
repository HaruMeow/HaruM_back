from django.shortcuts import render
from django.views import View

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cal/calendar.html')

class AddView(View):
    def get(self, request, *args, **kwargs):
        # AddView에서 필요한 처리를 여기에 추가
        return render(request, 'cal/add.html')

class MemoView(View):
    def get(self, request, *args, **kwargs):
        # MemoView에서 필요한 처리를 여기에 추가
        return render(request, 'cal/memo.html')

class TargetView(View):
    def get(self, request, *args, **kwargs):
        # TargetView에서 필요한 처리를 여기에 추가
        return render(request, 'cal/target.html')

class StateView(View):
    def get(self, request, *args, **kwargs):
        # StateView에서 필요한 처리를 여기에 추가
        return render(request, 'cal/state.html')
