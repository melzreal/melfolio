from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import (
    PageChooserPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks


class HomePage(Page):
    lead_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        [
            ("cta", blocks.CTABlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("left_card_block", blocks.LeftCardBlock()),
            ("right_card_block", blocks.RightCardBlock()),
            ("three_image_block", blocks.ThreeCardBlock()),
            ("two_image_block", blocks.TwoImageBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("lead_image"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
