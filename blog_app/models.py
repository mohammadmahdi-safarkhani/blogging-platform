from django.db import models
from blog_project import settings
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True)
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug                                        # this make the slug and if there is same 
            counter = 1                                             # slug, adds a number at hte end (must the slug field be blank=True)
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    
#-----------------------maybe use these in future-----------------------------------------------------------------
    # Field	        Type	            Use
    # excerpt	    TextField	        A short summary to show in post list
    # image	        ImageField	        Cover image for the post
    # tags	        ManyToManyField	    Use a tag system (django-taggit or your own)
    # category	    ForeignKey	        If you group posts under categories
    # views_count	IntegerField	    Track number of views
    # is_featured	BooleanField	    Highlight certain posts
#--------------------------------------------------------------------------------------------
