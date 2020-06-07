from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from phone_field import PhoneField
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField

# Create your models here.
CATEGORY_OPTIONS = (
    ('Technology', 'Technology'),
    ('Health', 'Health'),
    ('International', 'International'),
    ('Politics', 'Politics'),
    ('Society', 'Society'),
    ('Economics', 'Economics'),
    ('Education', 'Education'),
    ('Tourism', 'Tourism'),
    ('Development', 'Development'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion'),
    ('Entertainment', 'Entertainment')
)
FEATURED_OPTIONS = (
    ('True', 'True'),
    ('False','False'),
)

STATUS_OPTION = (
    (0, 'Draft'),
    (1, 'Published')
)

User = get_user_model()

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    title = models.CharField(max_length=255, verbose_name="Title",choices=CATEGORY_OPTIONS)
    slug=models.SlugField(unique=True, max_length=200,blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)




#class AuthorFollowLinks(models.Model):
    #facebook_link = models.URLField(blank=True, null=True)
    #twitter_link = models.URLField(blank=True, null=True)
    #google_plus_link = models.URLField(blank=True, null=True)
    #instagram_link = models.URLField(blank=True, null=True)

    #class Meta:
        #verbose_name_plural = 'Authors Follow Link'

    #def __str__(self):
        #return 'Facebook Link: ' + self.facebook_link

class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    phone = PhoneField(verbose_name="Phone No" ,help_text='Contact phone number')
    image= models.ImageField(upload_to='authorImages/', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="Short Info")
    #links = models.OneToOneField(AuthorFollowLinks, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.get_full_name()



class Post(models.Model):
    title=models.CharField(max_length=200, unique=True, verbose_name = 'Title')
    description=HTMLField()
    image=models.ImageField(upload_to='blogPostImages/')
    posted=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, max_length=200,blank=True)
    feature=models.CharField(max_length=100, verbose_name='Features', choices=FEATURED_OPTIONS)
    category=models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT, blank=True, null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_OPTION, default=1)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-posted']


    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
