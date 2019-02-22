from django.shortcuts import render
def index(req):
    msg = 'my message'
    return render(req, 'index.html', {'message':msg})

