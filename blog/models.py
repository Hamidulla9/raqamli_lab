from ckeditor.fields import RichTextField
from django.db import models


class Yangilik(models.Model):
    image = models.ImageField(upload_to='yangiliklar/')
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Loyiha(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='loyihalar/')
    link = models.URLField()
    github_link = models.URLField()
    star = models.BooleanField(default=True)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Hodim(models.Model):
    ism = models.CharField(max_length=100)
    description = RichTextField()
    yonalish = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hodimlar/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ism


class Taklif(models.Model):
    image = models.ImageField(upload_to='takliflar/')
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Takliflarimiz(models.Model):
    takliflar = models.ManyToManyField(Taklif)

    def __str__(self):
        return f'Takliflar: {", ".join(str(t) for t in self.takliflar.all())}'


class Boglanish(models.Model):
    longitud = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    description = RichTextField()
    telefon = models.CharField(max_length=255, blank=True, null=True)
    gmail = models.EmailField()
    telegram_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.telefon}"
