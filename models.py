from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField('Hotels name', max_length=50, help_text="Enter field name")
    qstars = models.CharField('How many stars', max_length=50)
    qfloor = models.IntegerField('Number of froors')
    qroom = models.IntegerField('How many rooms')
#    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.hotel_name

class Rooms(models.Model):
    num = models.IntegerField('Room number', help_text="")
    room_name = models.CharField('Room name', max_length=50, help_text="")
    view_from_the_window = models.CharField('View from the window', max_length=50, help_text="")
    price = models.CharField('Price', max_length=50, help_text="Enter field name")
    free = models.CharField('Free', max_length=50, help_text="Enter field name")
#    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.room_name