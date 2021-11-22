import uuid
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.conf import settings


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.profile.user.id, filename)

EXTERNAL_WORKS = (
    ('Gates', 'GATES'),
    ('Landscaping', 'LANDSCAPING'),
    ('Fences', 'FENCES'),
)

FITTINGS_FURNISHINGS = (
    ('Equipments', 'EQUIPMENTS'),
    ('Furnitures', 'FURNITURES'),
)

GENERAL_FINISHES = (
    ('Paints', 'PAINTS'),
)

INTERNAL_FINISHES = (
    ('Floor Finishes', 'FLOOR FINISHES'),
    ('Tiles', 'TILES'),
)

SUPERSTRUCTURE = (
    ('Glass', 'GATES'),
    ('Openings', 'OPENINGS'),
    ('Railing', 'RAILINGS'),
)


CATEGORIES= (
    ('External Works',EXTERNAL_WORKS),
    ('Fittings and Furnishings',FITTINGS_FURNISHINGS),
    ('Genearal Finishes',GENERAL_FINISHES),
    ('Internal Finishes',INTERNAL_FINISHES),
    ('Structure','STRUCTURE'),
    ('Superstructure',SUPERSTRUCTURE),
    ('Taps','TAPS'),
    ('Tools and Equipment','TOOLS & EQUIPMENTS'),

)

TYPES =(    
    ('Buy', 'BUY'),
    ('Rent', 'RENT'), 
)

CONDITIONS =(    
    ('New', 'NEW'),
    ('Used', 'USED'), 
    ('Manufacturer Refurbished', 'MANUFACTURER REFURBISHED'), 
    ('For Parts & Not Working', 'FOR PARTS & NOT WORKING'), 
)

GENDER = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Other','OTHER'),
)

class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    business_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = PhoneNumberField(null = True, blank = True)
    gender = models.CharField(choices=GENDER, max_length=55)
    location = models.CharField(max_length=55)
    bio = models.TextField(max_length=120, null=True)
    avatar = CloudinaryField('image')
    youtube = models.URLField(max_length=250, null=True, blank=True)
    facebook = models.URLField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(max_length=250, null=True, blank=True)
    twitter = models.URLField(max_length=250, null=True, blank=True)
    instagram = models.URLField(max_length=250, null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    is_vendor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    def save_image(self):
        self.save()      
        
    def delete_image(self):
        self.delete()
        
    def get_product_no(self, username):
        user = get_object_or_404(User, username=username)
        return Product.objects.filter(user=user).count()
    
    def get_product(self, username):
        user = get_object_or_404(User, username=username)
        return Product.objects.filter(user=user)
    
    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id=id).update(avatar=value)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        VendorProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    category  = models.CharField(choices=CATEGORIES, max_length=55)
    price = models.IntegerField(default=0)
    negotiatable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=TYPES, max_length=55)
    condition = models.CharField(choices=CONDITIONS, max_length=55)
    view = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    precise_location = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null = True, blank = True)
    negotiatable = models.BooleanField(default=False)
    agreement = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()
        
    @classmethod
    def search_products(cls,search_term):
        items = Product.objects.filter(product_name__icontains=search_term)
        return items
        
    def delete_image(self):
        self.delete()  
        
    def no_of_rating(self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)
    

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='rater_user')
    score = models.IntegerField(default=0, validators= [MaxValueValidator(5), MinValueValidator(1)])
    
    def __str__(self):
        return self.product.title

class Review(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='post_comment')
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='user_ratings')
    purchased = models.BooleanField(default=False)
    
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='commenter_profile')

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
    wished_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    # slug = models.CharField(max_length=30,null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item.title




















































































    