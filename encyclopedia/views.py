from django.http.response import HttpResponse
from django.shortcuts import render

from . import util
import encyclopedia

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getentry(request, title):
    return render(request, "encyclopedia/getentry.html", {
        "entry":util.get_entry(title), "title":title
    })
    
def search(request):
    if util.get_entry(request.GET.get("q")) != None:
        return render(request, "encyclopedia/getentry.html", {
        "entry":util.get_entry(request.GET.get("q")), "title":request.GET.get("q")
    })

    else:
        filenames = util.list_entries()
        substr_list = []
        for file in filenames:
            if request.GET.get("q") in file.lower():
                 substr_list.append(file)

            else:
                pass
        if len(substr_list) == 0:
            return render(request, "encyclopedia/no_such_entry.html")
        
        else:
            return render(request, "encyclopedia/search.html", {
                "substr_list":substr_list
            })

