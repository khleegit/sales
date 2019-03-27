from django.shortcuts import render

def post_list(request):
    return render(request, 'pap/post_list.html', {})