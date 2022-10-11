from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

class Category(models.Model):

    name = models.CharField(_("name"), max_length=200)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Post(models.Model):
    class PostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    options =(
        ('draft' , 'Draft'),
        ('published' , 'Published')
    )
    category = models.name = models.ForeignKey(Category, on_delete=models.PROTECT , default=1)
    title = models.CharField(_("title"), max_length=350)
    excerpt = models.TextField(_("excerpt"),null=True)
    content = models.TextField(_("content"))
    slug = models.SlugField(_("slug"),max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options,default='published')
    objects = models.Manager() #default manager
    postobject = PostObject() #custom manager

    class Meta:
        ordering =('-published',)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
