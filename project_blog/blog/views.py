from _csv import reader

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from blog.models import Entry, Photo
from blog.forms import CreateEntryForm, CSVEntryForm


def show_all(request):
    multiadd = request.user.has_perm('blog.multiadd')
    context = {
        'entries': Entry.objects.all(),
        'multiadd': multiadd
    }
    return render(request, 'blog/index.html', context=context)


def detail_view(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    photos = Photo.objects.filter(entry=entry).all()
    context = {
        'entry': entry,
        'photos': photos
    }
    return render(request, 'blog/entry_item.html', context=context)


def create_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.method == 'POST':
        form = CreateEntryForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            entry = Entry.objects.create(
                title=title,
                content=content,
                author=user
            )
            entry.save()
            files = request.FILES.getlist('files')
            for file in files:
                instance = Photo.objects.create(
                    file=file,
                    entry=entry
                )
                instance.save()
            return redirect('/')
    else:
        form = CreateEntryForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create_entry.html', context=context)


def csv_entries(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.method == 'POST':
        form = CSVEntryForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file'].read()
            file_str = file.decode('utf-8').split('\n')
            csv_reader = reader(file_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                entry = Entry.objects.create(
                    title=row[0],
                    content=row[1],
                    author=request.user
                )
                entry.save()
            return redirect('/')
    else:
        form = CSVEntryForm()
    context = {
        'form': form
    }
    return render(request, 'blog/csv_multiadd.html', context=context)
