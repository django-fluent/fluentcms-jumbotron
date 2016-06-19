"""
Definition of the plugin.
"""
from django.utils.translation import ugettext_lazy as _
from fluent_contents.extensions import ContentPlugin, plugin_pool
from .models import JumbotronItem


@plugin_pool.register
class JumbotronPlugin(ContentPlugin):
    """
    CMS plugin for previous/next navigation element.
    """
    category = _("Landing page")
    model = JumbotronItem
    render_template = "fluentcms_jumbotron/jumbotron.html"
    fieldsets = (
        (None, {
            'fields': ('title', 'content'),
        }),
        (_("Buttons"), {
            'fields': (
                ('button1_title', 'button2_title'),
                ('button1_url', 'button2_url'),
            ),
        }),
    )
