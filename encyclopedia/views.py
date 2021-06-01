from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getentry(request, title):
    return render(request, "encyclopedia/getentry.html", {
        "entry":util.get_entry(title), "title":title
    })
    

