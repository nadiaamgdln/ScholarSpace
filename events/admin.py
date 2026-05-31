from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from django.utils import timezone
from .models import Event, Category, Registration, Bookmark


# ─── CATEGORY ────────────────────────────────────────────────────────────────
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['icon_name', 'slug', 'color_preview', 'event_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

    def icon_name(self, obj):
        return format_html('<span style="font-size:1.2rem;">{}</span> <strong>{}</strong>', obj.icon, obj.name)
    icon_name.short_description = 'Kategori'

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:18px;height:18px;border-radius:4px;background:{};vertical-align:middle;margin-right:6px;"></span>{}',
            obj.color, obj.color
        )
    color_preview.short_description = 'Warna'

    def event_count(self, obj):
        return obj.event_count
    event_count.short_description = 'Jumlah Event'
    event_count.admin_order_field = 'event_count'

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(event_count=Count('event'))


# ─── EVENT ────────────────────────────────────────────────────────────────────
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = [
        'poster_thumb', 'title', 'category_badge', 'organizer',
        'status_badge', 'type_badge', 'deadline_display',
        'reg_count', 'is_featured',
    ]
    list_filter   = ['status', 'event_type', 'category', 'is_featured']
    search_fields = ['title', 'organizer', 'description']
    list_editable = ['is_featured']
    ordering      = ['-created_at']
    date_hierarchy = 'event_date'
    readonly_fields = ['created_at', 'poster_preview', 'reg_count']

    fieldsets = (
        ('📋 Informasi Dasar', {
            'fields': ('title', 'category', 'organizer', 'description'),
        }),
        ('📅 Waktu & Lokasi', {
            'fields': ('event_date', 'deadline', 'event_type', 'location', 'link_online'),
        }),
        ('💰 Detail & Persyaratan', {
            'fields': ('price', 'benefit', 'requirement'),
        }),
        ('🖼️ Poster', {
            'fields': ('poster', 'poster_preview'),
        }),
        ('⚙️ Pengaturan', {
            'fields': ('status', 'is_featured', 'created_at'),
        }),
    )

    # ── custom columns ──
    def poster_thumb(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="width:52px;height:36px;object-fit:cover;border-radius:6px;">', obj.poster.url)
        icon = obj.category.icon if obj.category else '📌'
        return format_html('<span style="font-size:1.6rem;">{}</span>', icon)
    poster_thumb.short_description = ''

    def poster_preview(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="max-width:340px;border-radius:10px;">', obj.poster.url)
        return '—'
    poster_preview.short_description = 'Preview Poster'

    def category_badge(self, obj):
        if obj.category:
            return format_html(
                '<span style="background:rgba(59,130,246,.15);color:#93c5fd;padding:2px 8px;border-radius:99px;font-size:12px;">'
                '{} {}</span>', obj.category.icon, obj.category.name)
        return '—'
    category_badge.short_description = 'Kategori'

    def status_badge(self, obj):
        colors = {'open': ('#34d399','#052e16'), 'closed': ('#f87171','#2d0a0a'), 'upcoming': ('#fbbf24','#2d1b00')}
        bg, fg = colors.get(obj.status, ('#999','#000'))
        return format_html(
            '<span style="background:{};color:{};padding:2px 10px;border-radius:99px;font-size:12px;font-weight:600;">{}</span>',
            bg, fg, obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def type_badge(self, obj):
        colors = {'online': '#22d3ee', 'offline': '#a78bfa', 'hybrid': '#fb923c'}
        color = colors.get(obj.event_type, '#999')
        return format_html(
            '<span style="color:{};font-size:12px;font-weight:600;">{}</span>',
            color, obj.get_event_type_display()
        )
    type_badge.short_description = 'Tipe'

    def deadline_display(self, obj):
        now = timezone.now()
        diff = obj.deadline - now
        if diff.days < 0:
            color, label = '#f87171', f'Lewat {abs(diff.days)}h'
        elif diff.days <= 3:
            color, label = '#fbbf24', f'⚠️ {diff.days}h lagi'
        else:
            color, label = '#86efac', obj.deadline.strftime('%d %b %Y')
        return format_html('<span style="color:{};font-size:12px;">{}</span>', color, label)
    deadline_display.short_description = 'Deadline'

    def reg_count(self, obj):
        n = obj.registrations.count()
        return format_html('<strong style="color:#93c5fd;">{}</strong>', n)
    reg_count.short_description = '👥 Pendaftar'

    # ── actions ──
    actions = ['mark_open', 'mark_closed', 'mark_featured', 'unmark_featured']

    def mark_open(self, request, qs):
        qs.update(status='open')
        self.message_user(request, f'{qs.count()} event diset ke Open ✅')
    mark_open.short_description = '✅ Set status → Open'

    def mark_closed(self, request, qs):
        qs.update(status='closed')
        self.message_user(request, f'{qs.count()} event diset ke Closed ❌')
    mark_closed.short_description = '❌ Set status → Closed'

    def mark_featured(self, request, qs):
        qs.update(is_featured=True)
        self.message_user(request, f'{qs.count()} event ditampilkan sebagai Featured ⭐')
    mark_featured.short_description = '⭐ Tandai sebagai Featured'

    def unmark_featured(self, request, qs):
        qs.update(is_featured=False)
        self.message_user(request, f'{qs.count()} event dihapus dari Featured')
    unmark_featured.short_description = '☆ Hapus dari Featured'


# ─── REGISTRATION ─────────────────────────────────────────────────────────────
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display  = ['name', 'npm', 'batch_year', 'email', 'phone', 'event_link', 'created_at']
    list_filter   = ['batch_year', 'event__category', 'event']
    search_fields = ['name', 'npm', 'email', 'event__title']
    ordering      = ['-created_at']
    readonly_fields = ['created_at']

    fieldsets = (
        ('👤 Data Peserta', {
            'fields': ('name', 'npm', 'email', 'phone', 'batch_year'),
        }),
        ('📝 Event & Motivasi', {
            'fields': ('event', 'motivation', 'created_at'),
        }),
    )

    def event_link(self, obj):
        return format_html(
            '<a href="/event/{}/" style="color:#93c5fd;" target="_blank">{}</a>',
            obj.event.pk, obj.event.title[:40]
        )
    event_link.short_description = 'Event'

    actions = ['export_emails']

    def export_emails(self, request, qs):
        emails = ', '.join(qs.values_list('email', flat=True))
        self.message_user(request, f'📧 Email terpilih: {emails}')
    export_emails.short_description = '📧 Tampilkan email terpilih'


# ─── BOOKMARK ─────────────────────────────────────────────────────────────────
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display  = ['user', 'event_title', 'created_at']
    list_filter   = ['event__category']
    search_fields = ['user__username', 'event__title']
    ordering      = ['-created_at']

    def event_title(self, obj):
        return obj.event.title
    event_title.short_description = 'Event'


# ─── ADMIN SITE BRANDING ──────────────────────────────────────────────────────
admin.site.site_header  = '🚀 USK TechHub Admin'
admin.site.site_title   = 'USK TechHub'
admin.site.index_title  = 'Panel Administrasi USK TechHub'
