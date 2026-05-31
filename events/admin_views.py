from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Count
from .models import Event, Category, Registration, Bookmark

@staff_member_required
def dashboard(request):
    total_events = Event.objects.count()
    open_events = Event.objects.filter(status='open').count()
    total_registrations = Registration.objects.count()
    total_categories = Category.objects.count()
    recent_events = Event.objects.order_by('-created_at')[:5]
    recent_regs = Registration.objects.order_by('-created_at')[:5]
    top_categories = Category.objects.annotate(cnt=Count('event')).order_by('-cnt')[:5]
    ctx = {
        'total_events': total_events,
        'open_events': open_events,
        'total_registrations': total_registrations,
        'total_categories': total_categories,
        'recent_events': recent_events,
        'recent_regs': recent_regs,
        'top_categories': top_categories,
    }
    return render(request, 'admin_panel/dashboard.html', ctx)

@staff_member_required
def event_list(request):
    events = Event.objects.annotate(reg_count=Count('registrations')).order_by('-created_at')
    return render(request, 'admin_panel/event_list.html', {'events': events})

@staff_member_required
def event_add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        e = Event(
            title=request.POST['title'],
            organizer=request.POST['organizer'],
            description=request.POST['description'],
            event_date=request.POST['event_date'],
            deadline=request.POST['deadline'],
            location=request.POST.get('location', ''),
            link_online=request.POST.get('link_online', ''),
            event_type=request.POST['event_type'],
            price=request.POST.get('price', 'Gratis'),
            benefit=request.POST.get('benefit', ''),
            requirement=request.POST.get('requirement', ''),
            status=request.POST['status'],
            is_featured='is_featured' in request.POST,
        )
        cat_id = request.POST.get('category')
        if cat_id:
            e.category_id = cat_id
        if 'poster' in request.FILES:
            e.poster = request.FILES['poster']
        e.save()
        messages.success(request, 'Event berhasil ditambahkan!')
        return redirect('admin_event_list')
    return render(request, 'admin_panel/event_form.html', {'categories': categories, 'action': 'Tambah'})

@staff_member_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        event.title = request.POST['title']
        event.organizer = request.POST['organizer']
        event.description = request.POST['description']
        event.event_date = request.POST['event_date']
        event.deadline = request.POST['deadline']
        event.location = request.POST.get('location', '')
        event.link_online = request.POST.get('link_online', '')
        event.event_type = request.POST['event_type']
        event.price = request.POST.get('price', 'Gratis')
        event.benefit = request.POST.get('benefit', '')
        event.requirement = request.POST.get('requirement', '')
        event.status = request.POST['status']
        event.is_featured = 'is_featured' in request.POST
        cat_id = request.POST.get('category')
        if cat_id:
            event.category_id = cat_id
        if 'poster' in request.FILES:
            event.poster = request.FILES['poster']
        event.save()
        messages.success(request, 'Event berhasil diupdate!')
        return redirect('admin_event_list')
    return render(request, 'admin_panel/event_form.html', {'event': event, 'categories': categories, 'action': 'Edit'})

@staff_member_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event berhasil dihapus.')
    return redirect('admin_event_list')

@staff_member_required
def category_list(request):
    cats = Category.objects.annotate(event_count=Count('event'))
    return render(request, 'admin_panel/category_list.html', {'categories': cats})

@staff_member_required
def category_add(request):
    if request.method == 'POST':
        c = Category(
            name=request.POST['name'],
            slug=request.POST['slug'],
            icon=request.POST.get('icon', '🏆'),
            color=request.POST.get('color', '#3b82f6'),
        )
        c.save()
        messages.success(request, 'Kategori ditambahkan!')
        return redirect('admin_category_list')
    return render(request, 'admin_panel/category_form.html')

@staff_member_required
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        cat.delete()
        messages.success(request, 'Kategori dihapus.')
    return redirect('admin_category_list')

@staff_member_required
def registration_list(request):
    regs = Registration.objects.select_related('event').order_by('-created_at')
    event_filter = request.GET.get('event', '')
    if event_filter:
        regs = regs.filter(event_id=event_filter)
    events = Event.objects.all()
    return render(request, 'admin_panel/registration_list.html', {'registrations': regs, 'events': events, 'event_filter': event_filter})

@staff_member_required
def registration_delete(request, pk):
    reg = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        reg.delete()
        messages.success(request, 'Data pendaftar dihapus.')
    return redirect('admin_registration_list')

@staff_member_required
def registration_detail(request, pk):
    reg = get_object_or_404(Registration, pk=pk)
    return render(request, 'admin_panel/registration_detail.html', {'reg': reg})
