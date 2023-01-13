# from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# # users
# class User(AbstractUser):
#     email = models.E

# cinema side

class Film(models.Model):
    name = models.CharField(max_length=255)
    ageRating = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    shortTrailerDescription = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Screen(models.Model):
    screen_number = models.PositiveSmallIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.screen_number)


class Showing(models.Model):
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    screen = models.ForeignKey(Screen, on_delete=models.PROTECT)
    time = models.DateTimeField()

class Ticket(models.Model):
    TICKET_TYPE_STUDENT = 'S'
    TICKET_TYPE_ADULT = 'A'
    TICKET_TYPE_CHILD = 'C'

    TICKET_TYPE_CHOICE = [
        (TICKET_TYPE_STUDENT, 'Student'),
        (TICKET_TYPE_ADULT, 'Adult'),
        (TICKET_TYPE_CHILD, 'Child'),
    ]

    ticket_type = models.CharField(max_length=1, choices=TICKET_TYPE_CHOICE, default=TICKET_TYPE_STUDENT)

    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)

    PRICE_CHOICE = [
        (TICKET_TYPE_STUDENT, '10'),
        (TICKET_TYPE_ADULT, '15'),
        (TICKET_TYPE_CHILD, '5'),
    ]

    ticket_price = models.CharField(max_length=1, choices=PRICE_CHOICE)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Address(models.Model):
    street_number = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.street_number + ' ' + self.street


class ContactDetails(models.Model):
    mobile_number = models.CharField(max_length=50)
    landline_number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email

class PaymentDetails(models.Model):
    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    expiry_date = models.DateField()


# club side

class Club(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE, null=True)
    club_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.club_name

class ClubRepresentative(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE, related_name='clubRep')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    club_representative_number = models.IntegerField(unique=True)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        ordering = ['first_name']
    

class Account(models.Model):
    club = models.OneToOneField(Club, on_delete=models.PROTECT)
    payment_details = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255, primary_key=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)


# unsure about this class, made it to keep a list of all accounts
class Order(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.PROTECT)
    account = models.OneToOneField(Account, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # class Meta:
    #     odering - ['user__first_name', 'user__last_name']