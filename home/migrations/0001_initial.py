# Generated by Django 3.1.3 on 2021-11-24 20:23

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=80, required=True))])), ('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('left_card_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=80, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('richtext', wagtail.core.blocks.RichTextBlock(required=True)), ('button', wagtail.core.blocks.StructBlock([('button_title', wagtail.core.blocks.CharBlock(help_text='Enter text to be displayed on the button', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page is selected, that will be used instead', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False))]))])))])), ('right_card_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=80, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('richtext', wagtail.core.blocks.RichTextBlock(required=True)), ('button', wagtail.core.blocks.StructBlock([('button_title', wagtail.core.blocks.CharBlock(help_text='Enter text to be displayed on the button', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page is selected, that will be used instead', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False))]))])))])), ('three_image_block', wagtail.core.blocks.StructBlock([('image_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image_one', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_two', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_three', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('two_image_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('lead_text', wagtail.core.blocks.TextBlock(help_text='Add your lead text', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('image_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image_one', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_two', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True)),
                ('lead_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
