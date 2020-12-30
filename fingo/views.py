from django.shortcuts import render
from .forms import MyForm
from django.template import loader
from django.http import HttpResponse
from .static.py.merc import Mercader

# Create your views here.


def index(request):
    txt = ''
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            mercader = Mercader()
            info = myForm.cleaned_data['info'].split('\n')
            txt = []
            for i in info:
                txt.append(str(mercader.instruction_decoder(i)) + '\n')
    form = MyForm()
    return render(request, 'fingo/index.html', {'form': form, 'txt': txt})
