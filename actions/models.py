from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey('auth.User', related_name='actions',
                             db_index=True, on_delete=models.CASCADE)
    # внешний ключ на модель ContentType;
    target_ct = models.ForeignKey(ContentType, blank=True, null=True,
                                  related_name='target_obj', on_delete=models.CASCADE)
    # PositiveIntegerField для хранения идентификатора на связанный объект;
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    # GenericForeignKey – поле для обращения к связанному объекту на
    # основании его типа и ID.
    target = GenericForeignKey('target_ct', 'target_id')
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
