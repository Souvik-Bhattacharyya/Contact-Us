from django.shortcuts import render, redirect, reverse
from . import models


def index_view(request):
    projects = models.Project.objects.all()[:10]
    reviews = models.Review.objects.all()[:5]
    return render(request, 'index.html', {'projects': projects, 'rv': reviews[0], 'reviews': reviews[1:]})


def project_view(request, category=None):
    if category == None or category == -1:
        projects = models.Project.objects.all()
    elif category == 0:
        projects = models.Project.objects.filter(category='0')
    elif category == 1:
        projects = models.Project.objects.filter(category='1')
    elif category == 2:
        projects = models.Project.objects.filter(category='2')
    elif category == 3:
        projects = models.Project.objects.filter(category='3')
    return render(request, 'our_projects.html', {'projects': projects})


def gallery_view(request):
    images = models.ProjectImage.objects.all()
    return render(request, 'gallery.html', {'images': images})


def about_view(request):
    return render(request, 'about_us.html')


def contact_view(request):
    status = 0
    if request.method == 'POST':
        if 'name' in request.POST and 'contact' in request.POST and 'message' in request.POST:
            contact = models.ContactUs(
                name=request.POST['name'], contact=request.POST['contact'], message=request.POST['message'])
            contact.save()
            status = 1
        else:
            status = -1
    return render(request, 'contact_us.html', {'status': status})


def details_view(request, prj_id):
    try:
        project = models.Project.objects.get(id=prj_id)
    except models.Project.DoesNotExist:
        return redirect(reverse('index'))
    imgs = models.ProjectImage.objects.filter(project=project)
    return render(request, 'details.html', {'imgs': imgs, 'project': project})
