# Generated by Django 3.2 on 2021-04-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0034_organization_other_names"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="billdocument",
            name="extras",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="billversion",
            name="extras",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="event",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="eventagendaitem",
            name="extras",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="jurisdiction",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="membership",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="links",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="organization",
            name="other_names",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="organization",
            name="sources",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="person",
            name="current_role",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="person",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="A key-value store for storing arbitrary information not covered elsewhere.",
            ),
        ),
        migrations.AlterField(
            model_name="voteevent",
            name="extras",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]