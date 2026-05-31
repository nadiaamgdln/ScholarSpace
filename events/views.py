from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from .models import Event, Category, Registration, Bookmark

def landing(request):
    featured  = Event.objects.filter(status='open', is_featured=True).order_by('-created_at')[:3]
    latest    = Event.objects.filter(status='open').order_by('-created_at')[:6]
    categories = Category.objects.annotate(event_count=Count('event')).order_by('-event_count')
    hero_preview = Event.objects.filter(status='open').order_by('-created_at')[:3]
    total_events = Event.objects.count()
    open_events  = Event.objects.filter(status='open').count()
    total_reg    = Registration.objects.count()
    ctx = {
        'featured': featured, 'latest': latest, 'categories': categories,
        'hero_preview': hero_preview, 'total_events': total_events,
        'open_events': open_events, 'total_reg': total_reg,
        'bookmarked_ids': _get_bookmarks(request),
    }
    return render(request, 'events/landing.html', ctx)

def explore(request):
    events     = Event.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    q              = request.GET.get('q', '')
    category_slug  = request.GET.get('category', '')
    status_filter  = request.GET.get('status', '')
    type_filter    = request.GET.get('type', '')
    if q:             events = events.filter(Q(title__icontains=q)|Q(organizer__icontains=q))
    if category_slug: events = events.filter(category__slug=category_slug)
    if status_filter: events = events.filter(status=status_filter)
    if type_filter:   events = events.filter(event_type=type_filter)
    ctx = {
        'events': events, 'categories': categories, 'q': q,
        'category_slug': category_slug, 'status_filter': status_filter,
        'type_filter': type_filter, 'bookmarked_ids': _get_bookmarks(request),
    }
    return render(request, 'events/explore.html', ctx)

def event_detail(request, pk):
    event   = get_object_or_404(Event, pk=pk)
    related = Event.objects.filter(category=event.category).exclude(pk=pk)[:3]
    is_bookmarked = (
        request.user.is_authenticated and
        Bookmark.objects.filter(user=request.user, event=event).exists()
    )
    return render(request, 'events/detail.html', {
        'event': event, 'related': related, 'is_bookmarked': is_bookmarked,
        'bookmarked_ids': _get_bookmarks(request),
    })

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.status != 'open':
        messages.error(request, 'Pendaftaran event ini sudah ditutup.')
        return redirect('event_detail', pk=pk)
    if request.method == 'POST':
        Registration.objects.create(
            event=event,
            name=request.POST['name'], npm=request.POST['npm'],
            email=request.POST['email'], phone=request.POST['phone'],
            batch_year=request.POST['batch_year'], motivation=request.POST['motivation'],
        )
        messages.success(request, f'Pendaftaran berhasil untuk {event.title}!')
        return redirect('event_detail', pk=pk)
    return render(request, 'events/register.html', {'event': event})

@login_required
def toggle_bookmark(request, pk):
    event = get_object_or_404(Event, pk=pk)
    bm, created = Bookmark.objects.get_or_create(user=request.user, event=event)
    if not created:
        bm.delete()
        bookmarked = False
    else:
        bookmarked = True
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'bookmarked': bookmarked})
    return redirect(request.META.get('HTTP_REFERER', 'event_detail'), pk=pk)

@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('event').order_by('-created_at')
    bookmarked_ids = list(bookmarks.values_list('event_id', flat=True))
    return render(request, 'events/bookmarks.html', {'bookmarks': bookmarks, 'bookmarked_ids': bookmarked_ids})

def _get_bookmarks(request):
    if request.user.is_authenticated:
        return list(Bookmark.objects.filter(user=request.user).values_list('event_id', flat=True))
    return []
