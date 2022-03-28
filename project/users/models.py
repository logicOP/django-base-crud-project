from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=100)

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                for field in self.__class__._meta.fields[2:]
                ]
