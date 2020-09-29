from django.db import models
from django.utils import timezone
from django.urls import reverse


UNIT_TYPE = (
    ('CHALEH','CHALEH'),
    ('ROOM' , 'ROOM'),
    ('FLAT' , 'FLAT'),
    ('STUDIO' , 'STUDIO'),
)

class Area(models.Model):
    title = models.CharField(max_length=60, verbose_name='Area', )

    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=60, verbose_name='City', )
    #area = models.ManyToManyField(Area)

    def __str__(self):
        return self.title

class Country(models.Model):
    title = models.CharField(max_length=60, verbose_name='Country', )
    #city = models.ManyToManyField(City)

    def __str__(self):
        return self.title

class Amenity(models.Model):
    title = models.CharField(max_length=60, verbose_name='Amenity', )

    def __str__(self):
        return self.title


class Unit(models.Model):

    title = models.CharField(max_length=60, verbose_name='Unit Title', )
    description = models.TextField(max_length=500, verbose_name='Unit Description')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    num_bedrooms = models.IntegerField( verbose_name='Number of Bed rooms')
    image = models.ImageField(upload_to='units_images/' , blank=True , null=True, verbose_name='Unit Main Image')
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    owner_email = models.EmailField(default='fahdkuwait@gmail.com')
    type = models.CharField(choices=UNIT_TYPE , default='ROOM',max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity)
    slug = models.SlugField(null=False, unique=True)


    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ('-active',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('units:unit_detail', kwargs={'slug': self.slug})


class Images(models.Model):
    unit =  models.ForeignKey(Unit,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='units_images/')

    def __str__(self):
        return self.title