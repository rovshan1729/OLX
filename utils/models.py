from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PriceChoice(models.TextChoices):
    PRICE = 'цена'
    FREE = 'бесплатно'
    EXCHANGE = 'обмен'


class CurrencyChoice(models.TextChoices):
    SUM = 'сум'
    DOLLAR = 'y.e'


class PrivateBusinessChoice(models.TextChoices):
    PRIVATE_FIGURE = 'Частное лицо'
    LEGAL_ENTITY = 'Бизнес'


class ConditionChoice(models.TextChoices):
    NEW = 'Новый'
    USED = 'Б/у'


class OptionType(models.TextChoices):
    SELECT_BUTTON = 'Select_Button'
    NUMBER = 'Number'
    SELECT = 'Select'
    TEXT = 'Text'
    MULTIPLE_CHOICES = 'Multiple_Choice'


class StatusType(models.TextChoices):
    ACTIVE = 'Активный'
    INACTIVE = 'Неактивный'
    PROCESS = 'В прогрессе'
    NOT_PAYED = 'Не выплачиваеться'