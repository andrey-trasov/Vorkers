from django.db import models


class Vorkers(models.Model):  # фио номе бригады зп специализация
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    team_number = models.IntegerField(verbose_name="номер бригады")
    salary = models.IntegerField(verbose_name="зарплата")
    specialization = models.CharField(max_length=250, verbose_name="специализация")

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.full_name
