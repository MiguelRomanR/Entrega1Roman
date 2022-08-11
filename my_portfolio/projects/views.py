from django.shortcuts import render
from projects.models import Project

# Create your views here.


def search_projects(request):
    if request.method == "POST":
        searched = request.POST['searched']
        projects = Project.objects.filter(title__icontains=searched)

        return render(request, 'search_projects.html', {'searched': searched, 'projects': projects})
    else:
        return render(request, 'search_projects.html', {})


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
