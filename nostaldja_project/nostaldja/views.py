from django.shortcuts import render, redirect
# from .models import Decade, Fad
# from .forms import DecadeForm, FadForm

# Create your views here.


def decade_list(request):
    decades = Decade.objects.all().order_by('start_year')
    return render(request, 'nostaldja/decade_crud.html', {'decades': decades})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    fads = Fad.objects.filter(decade_id=pk)
    return render(request, 'nostaldja/decade_crud.html', {'decade': decade, 'fads': fads})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()

    return render(request, 'nostaldja/decade_crud.html', {'form': form})


def decade_update(request, pk):
    decade = Decade.objects.get(id=pk)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_create.html', {'form': form})


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_crud.html', {'fads': fads})


def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_crud.html', {'fad': fad})


def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_crud', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/fad_crud.html', {'form': form})


def fad_update(request, pk):
    fad = Fad.objects.get(id=pk)
    if request.method == 'POST':
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_create.html', {'form': form})


def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
