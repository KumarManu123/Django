from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def studentinput_view(request):
    form=StudentForm()
    my_dict={'form':form}
    return render(request,'mytest/info.html',my_dict)