from django.db import models
from django.contrib.auth import get_user_model
from utils.models import (
    BaseModel,
    PriceChoice,
    CurrencyChoice,
    PrivateBusinessChoice,
    ConditionChoice,
    StatusType
)

class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class SubCategory(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )
    
class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Districts(BaseModel):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='districts'
    )

    def __str__(self):
        return self.title
    
class Post(BaseModel):
    title = models.CharField(max_length=255)

    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='sub-category'
    )
    description = models.TextField()

    price_type = models.CharField(max_length=255, choices=PriceChoice.choices)
    currency = models.CharField(max_length=255, choices=CurrencyChoice.choices)
    price = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=255, choices=StatusType.choices)
    views = models.IntegerField(blank=True, null=True, editable=False, default=0)
    
    private_or_business_figure = models.CharField(
        max_length=255, choices=PrivateBusinessChoice.choices
    )
    condition = models.CharField(max_length=255, choices=ConditionChoice.choices)
    
    is_active = models.BooleanField(default=True)
    auto_renewal = models.BooleanField(default=False)
    location = models.ForeignKey(
        Districts, on_delete=models.CASCADE, related_name='location'
    )

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True,
        )

    contact_person_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()


    def __str__(self):
        return self.title

class Photo(BaseModel):
    image = models.ImageField(upload_to='media/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    @classmethod
    def get_main_photo(cls, post_id):
        photo = Photo.objects.filter(
            post_id=post_id, is_main=True, related_name='photos'
        )
        print(photo)
        if photo:
            return photo.image
        return None
    
class Chat(BaseModel):
    seller = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='seller'
    )
    buyer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='buyer'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='chat'
        )


class ChatMessage(BaseModel):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='chat'
    )
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()

    
