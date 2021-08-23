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
    with open(f'encyclopedia/templates/encyclopedia/{name}.html','w') as f:
        f.write(html)

    return render(request,f'encyclopedia/{name}.html') 
