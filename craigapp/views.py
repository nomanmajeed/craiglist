from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'craigapp/index.html')

def new_search(request):
    data = request.POST.get('search')
    #print(data)
    context = {'data':data}
    return render(request, 'craigapp/new_search.html', context)
