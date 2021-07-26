from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return f"MenuItem(name:{self.name}, code:{self.code})"


class TgProfile(models.Model):
    creation_time = models.DateTimeField(auto_now=True)
    tg_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return (
            f"TgProfile(tg_id:{self.tg_id},"
            f" username:{self.username},"
            f" first_name:{self.first_name},"
            f" second_name:{self.second_name})"
        )
