from django.db import models


class Profile(models.Model):
    external_id = models.PositiveBigIntegerField(
        verbose_name='ID of user\'s telegram',
        unique=True,
    )
    name = models.TextField(
        verbose_name='nickname of user\'s telegram',
    )
    invite_from = models.TextField(
        verbose_name='invite_from'
    )
    invited_users = models.PositiveIntegerField(
        verbose_name='invited_users'
    )


    class Meta:
        verbose_name = 'Profile'
