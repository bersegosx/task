# -*- coding: utf-8 -*-

import string

from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver

class ShortLink(models.Model):
    """ Ссылка """

    original_url   = models.URLField("Оригинальная ссылка", max_length=500, default=None)
    short_link     = models.CharField("Сокращенная ссылка", max_length=10, db_index=True)
    created_at     = models.DateTimeField("Дата создания", auto_now_add=True)
    redirect_count = models.PositiveIntegerField("Количество переходов", default=0)

    def inc_views(self):
        self.redirect_count += 1
        self.save()

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылка"
        ordering = ("-redirect_count", "-created_at",)

    @classmethod
    def create_short_link(cls, number):
        # http://www.manhunter.ru/webmaster/421_kak_sdelat_svoy_servis_korotkih_ssilok.html
        digits = string.digits + string.ascii_letters
        digits_count = len(digits)

        link = ""

        while number:
            number, ost = divmod(number, digits_count)
            link += digits[ost]

        return link

@receiver(post_save, sender=ShortLink)
def generate_short_link(sender, **kwargs):
    inst = kwargs.get("instance")
    if not inst:
        return

    if not inst.short_link:
        inst.short_link = ShortLink.create_short_link(inst.id)
        inst.save()