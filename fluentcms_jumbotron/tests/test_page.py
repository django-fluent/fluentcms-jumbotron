from django.template import Template, Context
from django.test import TestCase, override_settings, RequestFactory
from django.utils.html import strip_tags
from fluent_contents.models import Placeholder

from fluentcms_jumbotron.models import JumbotronItem
from .models import ExamplePage


class JumbotronTests(TestCase):
    """
    Testing jumbotrons
    """

    @classmethod
    def create_page(cls, slug, **jumbotron_kwargs):
        """
        Factory to create an page
        """
        page = ExamplePage.objects.create(slug=slug)
        placeholder = Placeholder.objects.create_for_object(page, slot='content')
        JumbotronItem.objects.create_for_placeholder(placeholder, **jumbotron_kwargs)
        return page

    @override_settings(FLUENT_CONTENTS_CACHE_OUTPUT=False)  # in runtests.py disabled
    def test_default_jumbotron(self):
        """
        Default jumbotron rendering
        """
        page1 = self.create_page(slug='page1', title="Hello", content="<p>test</p>", button_url='http://example.org/', button_title="GO")

        template = Template('{% load fluent_contents_tags %}{% page_placeholder "content" %}')
        request = RequestFactory().get("/", HTTP_HOST='example.org')

        html = template.render(Context({'page': page1, 'request': request}))
        expected = '''<div class="jumbotron">
  <div class="container">
    <h1>Hello</h1>
    <p>test</p>
    <p><a class="btn btn-primary btn-lg" href="http://example.org/" role="button">GO</a></p>
  </div>
</div>'''
        self.assertEqual(strip_tags(html).strip(), 'Hello\n    test\n    GO')
        self.assertEqual(html.strip(), expected)
