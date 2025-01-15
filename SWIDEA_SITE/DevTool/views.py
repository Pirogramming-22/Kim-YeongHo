from django.shortcuts import render,redirect
from .models import Devtool
from .forms import DevtoolForm

# Create your views here.
def toolManage(request):
    tools=Devtool.objects.all()
    return render(request , 'DevTool/index.html',{'tools':tools})

def toolDetail(request ,pk):
    if request.method == 'GET':
        tool = Devtool.objects.get(id=pk)
        relative_posts = tool.post_set.all()
        return render(request , 'DevTool/detail.html' , {'tool':tool , 'relative_posts':relative_posts})
    elif request.method == 'POST':
        tool= Devtool.objects.get(id=pk)
        tool.name =request.POST['name']
        tool.explanation =request.POST['explanation']
        tool.category =request.POST['category']
        tool.save()
        relative_posts = tool.post_set.all()
        return render(request , 'DevTool/detail.html' , {'tool':tool , 'relative_posts':relative_posts})

def toolRegister(request):
    if(request.method == 'POST'):
        form = DevtoolForm(request.POST)
        if form.is_valid():
            tool = form.save()
            return redirect('DevTool:toolDetail' , pk= tool.pk)
    form = DevtoolForm()
    return render(request , 'DevTool/create.html',{'form':form} )

def toolDelete(request,pk):
    tool = Devtool.objects.get(id=pk)
    tool.delete()
    return redirect('DevTool:toolManage')

def toolUpdate(request , pk):
    tool =Devtool.objects.get(id=pk)
    form = DevtoolForm(instance=tool)
    ctx={
        'tool' : tool,
        'form' : form,
        'pk' : pk
    }
    return render(request , 'DevTool/update.html' ,ctx)