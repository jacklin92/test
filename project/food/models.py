from django.db import models


class Account(models.Model):
    client_name = models.TextField(default="")
    email_address = models.TextField(default="")
    password = models.TextField(default="")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Account"
        constraints = [
            models.UniqueConstraint(fields=['email_address'], name='unique_email'),
        ]
