from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


# Мы регистрируем функцию users_like_changed как функцию-подписчик с помощью де-
# коратора receiver и подписываемся на сигнал m2m_changed, отправляемый связями Image.
# users_like.through. Использование декоратора – один из способов добавления функ-
# ции-подписчика. Кроме этого, можно использовать метод connect() объекта Signal.
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
