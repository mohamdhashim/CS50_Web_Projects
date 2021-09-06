from django.shortcuts import render
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
    
    name = name.lower() #to prevent making another Html copy if user input Url capitalized ex : wiki/Git same as wiki/git
    return render(request,f'encyclopedia/topic.html',{'content': html, 'topic': name}) 


def edit(request,name):

    with open (f"entries/{name.lower()}.md",'r') as f:
        text = f.read()
        full_text = ""
        for i in text:
            for t in i:
                full_text += t

    return render(request,f"encyclopedia/css.html") 


def search(request):

    q = request.GET['q']
    if q == '':
        return index(request) #if searching is empty say in the same page


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

    
   #return render(request,f'encyclopedia/search_results.html') 