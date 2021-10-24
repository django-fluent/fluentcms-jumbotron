from django.db import models
from fluent_contents.models import PlaceholderField


class ExamplePage(models.Model):
    slug = models.SlugField()
    content = PlaceholderField(slot='content')

    def __str__(self):
        return self.slug
