from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from fluent_contents.models import PlaceholderField


@python_2_unicode_compatible
class ExamplePage(models.Model):
    slug = models.SlugField()
    content = PlaceholderField(slot='content')

    def __str__(self):
        return self.slug
