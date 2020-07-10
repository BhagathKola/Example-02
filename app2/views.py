from django.shortcuts import render,redirect
from Project2.settings import COVID_19_FILE
import json
from app2.middleware import covid_19

def showIndex(request):
    dict_data = json.loads(open(COVID_19_FILE).read())
    states = [x for x in dict_data]
    states.pop(0)
    return render(request,"index.html",{"data":states})


def open_state(request):
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(COVID_19_FILE).read())
    return render(request,"state.html",{"sname":sname,"data":dict_data[sname]})


def refresh(request):
    covid_19()
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(COVID_19_FILE).read())
    return render(request, "state.html", {"sname": sname, "data": dict_data[sname]})
