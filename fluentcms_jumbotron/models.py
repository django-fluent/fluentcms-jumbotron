from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import PluginHtmlField, PluginUrlField
from fluent_contents.models import ContentItem


@python_2_unicode_compatible
class JumbotronItem(ContentItem):
    """
    Pager item, to show a previous/next page.
    The pages are auto determined, but can be overwritten
    """
    title = models.CharField(_("Title"), max_length=200)
    content = PluginHtmlField(_("Content"))  # TODO: replace with child elements later?
    button_title = models.CharField(_("Button Title"), max_length=200, blank=True, null=True)
    button_url = PluginUrlField(_("Button URL"), blank=True, null=True)

    class Meta:
        verbose_name = _("Jumbotron")
        verbose_name_plural = _("Jumbotron")

    def __str__(self):
        return self.title
