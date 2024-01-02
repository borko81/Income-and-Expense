from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime


class CheckOutModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    suma = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, amount available: {self.suma}"


TypesVid = (
    ("Income", "Income"),
    ("Expence", "Expence"),
    ("Income/Excome", "Income/Excome"),
    ("Begin", "Begin"),
)

mapper = {t1: t2 for t1, t2 in TypesVid}


class TypeOldData(models.Model):
    old_name = models.CharField(max_length=32, unique=True, null=False, blank=False)
    old_type = models.CharField(max_length=15, choices=TypesVid)
    date_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.date_updated)


class TypesManager(models.Manager):
    def only_with_filter(self, name):
        return self.get_queryset().filter(type_name=mapper[name])


class Types(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    type_name = models.CharField(max_length=15, choices=TypesVid)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    only_type = TypesManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id:
            self.date_updated = datetime.now()
            old_obj = Types.objects.get(id=self.id)
            TypeOldData.objects.create(
                old_name=old_obj.name,
                old_type=old_obj.type_name,
                date_updated=datetime.now(),
            )

        super(Types, self).save(*args, **kwargs)


class NewActionModel(models.Model):
    from_user = models.ForeignKey(
        CheckOutModel, on_delete=models.DO_NOTHING, related_name="from_user"
    )
    to_user = models.ForeignKey(
        CheckOutModel,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="to_user",
    )
    type_action = models.ForeignKey(Types, on_delete=models.DO_NOTHING)
    suma = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=120, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        from_user = CheckOutModel.objects.get(id=self.from_user.id)
        if from_user.suma + self.suma < 0:
            raise Exception("There is not enought money for transaction!")

        if self.id:
            self.date_updated = datetime.now()

        if (
            self.to_user
            and CheckOutModel.objects.get(id=self.from_user.id).suma + self.suma >= 0
        ):
            CheckOutModel.objects.filter(id=self.to_user.id).update(
                suma=F("suma") + abs(self.suma)
            )
            CheckOutModel.objects.filter(id=self.from_user.id).update(
                suma=F("suma") + self.suma
            )
        if not self.to_user:
            CheckOutModel.objects.filter(id=self.from_user.id).update(
                suma=F("suma") + self.suma
            )
        super(NewActionModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        kasa_in = CheckOutModel.objects.get(id=self.from_user.id)
        kasa_to = CheckOutModel.objects.get(id=self.to_user.id)
        kasa_in.suma -= self.suma
        kasa_in.save()
        if kasa_to:
            kasa_to.suma -= abs(self.suma)
            kasa_to.save()
        super(NewActionModel, self).delete(*args, **kwargs)

    def __str__(self):
        return self.from_user.name


# @receiver(pre_save, sender=NewActionModel)
# def validate_suma_for_transaction(sender, instance, **kwargs):
#     from_user = CheckOutModel.objects.get(id=instance.from_user.id)
#     print("Before validate", from_user, from_user.suma, instance.suma)
#     if from_user.suma + instance.suma < 0:
#         raise Exception("There is not enought money for transaction!")
#     print("After validate", from_user, from_user.suma)
