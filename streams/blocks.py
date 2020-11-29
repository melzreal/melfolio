from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class PageChooserBlockWithTitle(blocks.StructBlock):
    button_title = blocks.CharBlock(
        required=False, help_text="Enter text to be displayed on the button"
    )
    button_url = blocks.URLBlock(
        required=False,
        help_text="If the button page is selected, that will be used instead",
    )
    button_page = blocks.PageChooserBlock(required=False)


class LeftCardBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=80)),
                ("text", blocks.TextBlock(required=True)),
                ("richtext", blocks.RichTextBlock(required=True)),
                ("button", PageChooserBlockWithTitle()),
            ]
        )
    )

    class Meta:
        template = "streams/left_card_block.html"
        icon = "placeholder"
        label = "Left Card Block"


class RightCardBlock(LeftCardBlock):
    class Meta:
        template = "streams/right_card_block.html"
        icon = "placeholder"
        label = "Right Card Block"


class RichtextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "RichText Block"


class CTABlock(blocks.StructBlock):

    title = blocks.CharBlock()
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Learn More", max_length=80)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class ThreeCardBlock(blocks.StructBlock):

    image_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image_one", ImageChooserBlock(required=True)),
                ("image_two", ImageChooserBlock(required=True)),
                ("image_three", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/three_image_block.html"
        icon = "placeholder"
        label = "Three Image Block"


class TwoImageBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add your title")
    lead_text = blocks.TextBlock(required=True, help_text="Add your lead text")
    text = blocks.TextBlock(required=True, help_text="Add additional text")
    button_page = blocks.PageChooserBlock(required=False)
    image_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image_one", ImageChooserBlock(required=True)),
                ("image_two", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/two_image_block.html"
        icon = "form"
        label = "Two Image Block"


class ColumnWideImageBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/column_wide_image.html"
        icon = "image"
        label = "Column Wide Image Block"


class TwoColumnTextBlock(blocks.StructBlock):

    column_one_text = blocks.RichTextBlock(required=True)
    column_two_text = blocks.RichTextBlock(required=True)

    class Meta:
        template = "streams/two_column_text_block.html"
        icon = "list-ul"
        label = "Two Column Text Block"


