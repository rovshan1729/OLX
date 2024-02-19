from django.db import models
from utils.models import BaseModel, OptionType
from post.models import Post

class Option(BaseModel):
    title = models.CharField(max_length=255)
    option_type = models.CharField(max_length=255, choices=OptionType.choices)

    order = models.IntegerField(default=0)  
    regex = models.CharField(max_length=255, blank=True, null=True) 
    limit = models.IntegerField(blank=True, null=True)  
    place_holder = models.CharField(max_length=255, blank=True, null=True)  
    is_required = models.BooleanField(default=False)  

class OptionValue(BaseModel):
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name=''
    )
    value = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.value
    
class PostOption(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post-option'
        )
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name='option'
        )
    value = models.TextField()


class PostOptionValue(BaseModel):
    post_option = models.ForeignKey(
        PostOption, on_delete=models.CASCADE,related_name='post-option-value'
        )
    