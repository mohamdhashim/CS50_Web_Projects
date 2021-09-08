import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
import markdown 

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def topic(request,name):

    if(name.lower() not in util.list_entries()):
        return render(request,'encyclopedia/not_found.html',{'name':name})

    with open (f'entries/{name.lower()}.md','r') as f:
        text = f.read()
        html = markdown.markdown(text)
    
    name = name.lower()
    return render(request,f'encyclopedia/topic.html',{'content': html, 'topic': name}) 



def edit(request,name):

    with open (f"entries/{name.lower()}.md",'r') as f:
        text = f.read()
        full_text = ""
        for i in text:
            for t in i:
                full_text += t

    
    new_content = request.POST.get('new_text')
    if(new_content):
        util.save_entry(name, new_content)
        return topic(request, name)
        
    return render(request,f"encyclopedia/edit.html",{"text":full_text,"topic":"edit "+name}) 


def create(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('new_text')

        if  title == '':
            return render(request, f"encyclopedia/create.html", {"error":2})
        elif title in util.list_entries():
            return render(request, f"encyclopedia/create.html", {"error":1})
        else:
            util.save_entry(title.lower(), content)
            return redirect("topic",title)
    else:
        return render(request, f"encyclopedia/create.html")


def search(request):

    q = request.GET['q']
    if q == '':
        return index(request) #if searching is empty stay in the same page(Home page)


    if q.lower() in util.list_entries():
        return topic(request, q)
    
    else: 
        searched_list = []
        for entry in util.list_entries():
            if q in entry:
                searched_list.append(entry)
        
        return render(request, "encyclopedia/search_results.html", {
        "entries": searched_list ,"count" : len(searched_list)
        })

def random(request):

    import random
    return redirect("topic", random.choice(util.list_entries()))