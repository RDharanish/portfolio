from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def projects(request):
    project_show=[

        {'title':'Clinic Management System',
            'path':'images/cli.png',},
            {'title': 'Cerebral palsy',
            'path':'images/cp.png',},
           {'title':'Ecommerce',
            'path':'images/ec.png',},
            {'title':'weather dashboard',
            'path':'images/api.png',
        },
    ]
    return render(request,"projects.html",{"project_show":project_show})
def certificate(request):
    return render(request,"certificate.html")
def contact(request):
    return render(request,"contact.html")
def resume(request):
    resume_path="myapp/Dharanish_profile.pdf"
    resume_path= staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="Dharanish_profile.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)