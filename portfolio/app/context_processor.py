from . models import *

def personaldetail(request):
    personaldetail= PersonalDetail.objects.first()
    return{
        'personaldetail':personaldetail
    }