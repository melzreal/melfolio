from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks

class FlexPage(Page):
    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("column_wide_image", blocks.ColumnWideImageBlock()),
            ("cta", blocks.CTABlock()),
            ("left_card_block", blocks.LeftCardBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("right_card_block", blocks.RightCardBlock()),
            ("three_image_block", blocks.ThreeCardBlock()),
            ("two_column_text", blocks.TwoColumnTextBlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("two_image_block", blocks.TwoImageBlock()),
        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
