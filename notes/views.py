from django.shortcuts import render

def show_greetings(request):
    return render(request, 'notes/greeting.html')

