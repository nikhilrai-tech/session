from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def set(request):
    name=request.session["name"]="nikhil rai"
    email=request.session["email"]="nikhilrai662@gmail.com"
    return render(request,'set.html')
def get(request):
    name=request.session.get("name",None)
    email=request.session.get("email",None)
    return render(request,'get.html',{"Name":name,"Email":email})

def update(request):
    name=request.session["name"]="amit"
    email=request.session["email"]="amit@gmail.com"
    return render(request,'update.html')

def delete(request):
    request.session.flush()
    return render(request,'delete.html')
