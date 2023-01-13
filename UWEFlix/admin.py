from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models import Count
from . import models

# address and contact details
@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'street_number', 'city', 'postcode', 'club']

    def club(self, address):
        return address.club_set.name

        #  def screen_capacity(self, showing):
        # return showing.screen.capacity



@admin.register(models.ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['mobile_number', 'email'] 



# club and clubRep

@admin.register(models.ClubRepresentative)
class ClubRepresentativeAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'club']
    list_editable = ['first_name']
    list_per_page = 10



@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'club_name', 'clubRep', 'address', 'contact_details']
    
    def show_address(self, club):
        url = (reverse('admin:UWEFlix_address_changelist')
        + '?'
        + urlencode({
            'address__id': str(club.id)
        }))
        return format_html('<a href="{}">{}</a>', url, club.address)



# films and showing

@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'showing_count']
    search_fields = ['name__istartswith']

    @admin.display(ordering = 'showing_count')
    def showing_count(self, film):
        url = (reverse('admin:UWEFlix_showing_changelist') 
        + '?'
        + urlencode({
          'film__id': str(film.id) 
        })) 
        return format_html('<a href="{}">{}</a>', url, film.showing_count)
         
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            showing_count=Count('showing')
        )

@admin.register(models.Showing)
class ShowingAdmin(admin.ModelAdmin):
    list_display = ['film', 'time', 'screen', 'screen_capacity']
    list_filter = ['film_id', 'time']

    def screen_capacity(self, showing):
        return showing.screen.capacity




admin.site.register(models.Screen)
