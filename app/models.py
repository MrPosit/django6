from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Team(models.Model):
    class Sport(models.TextChoices):
        FOOTBALL = 'FB', 'Футбол'
        BASKETBALL = 'BS', 'Баскетбол'
        HOCKEY = 'HK', 'Хоккей'
        BASEBALL = 'BB', 'Бейсбол'
        VOLLEYBALL = 'VL', 'Волейбол'

    name = models.CharField(max_length=100, verbose_name='Команда')
    creation_year = models.IntegerField(validators=[MinValueValidator(1900)], verbose_name='Год создания')
    sport = models.CharField(max_length=2, choices=Sport.choices, verbose_name='Вид спорта')
    coach = models.CharField(max_length=100, verbose_name='Тренер')
    owner = models.CharField(max_length=100, verbose_name='Владелец')
    
    def __str__(self):
        return f"{self.name} ({self.creation_year}) - {self.get_sport_display()}"

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Player(models.Model):
    f_name = models.CharField(max_length=100, verbose_name='Имя')
    l_name = models.CharField(max_length=100, verbose_name='Фамилия')
    shirt_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Номер')
    height = models.FloatField(verbose_name='Рост')
    weight = models.FloatField(verbose_name='Вес')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} - {self.team.name} ({self.shirt_number})"

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Item(models.Model):
    titles =models.CharField(max_length=200, verbose_name='Заголовок')