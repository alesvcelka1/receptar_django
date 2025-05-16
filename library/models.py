from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Kuchar(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno kuchaře', help_text='Zadejte jméno kuchaře')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení kuchaře', help_text='Zadejte příjmení kuchaře')
    biografie = models.TextField(blank=True, verbose_name='Životopis')
    fotografie = models.ImageField(upload_to='kuchari/', verbose_name='Fotografie', blank=True, null=True)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Kuchař'
        verbose_name_plural = 'Kuchaři'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Kategorie(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název kategorie', help_text='Zadejte název kategorie')
    obrazek = models.ImageField(upload_to='kategorie/', blank=True, null=True, verbose_name='Obrázek kategorie')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazev



class Recept(models.Model):
    titul = models.CharField(max_length=100, verbose_name='Název receptu', help_text='Zadejte název receptu')
    kuchar = models.ForeignKey(Kuchar, on_delete=models.SET_NULL, null=True, verbose_name='Kuchař')
    popis = models.TextField(verbose_name='Popis receptu', help_text='Vložte popis receptu')
    ingredience = models.TextField(verbose_name='Ingredience', help_text='Vložte ingredience receptu')
    postup = models.TextField(verbose_name='Postup', help_text='Vložte postup přípravy')
    kategorie = models.ManyToManyField(Kategorie, verbose_name='Kategorie')
    obrazek = models.ImageField(upload_to='recepty/', verbose_name='Obrázek receptu', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Vytvořeno')
    updated = models.DateTimeField(auto_now=True, verbose_name='Upraveno')

    class Meta:
        ordering = ['titul']
        verbose_name = 'Recept'
        verbose_name_plural = 'Recepty'

    def __str__(self):
        return self.titul


class Recenze(models.Model):
    text = models.TextField(verbose_name='Text recenze', help_text='Vložte text recenze')
    upraveno = models.DateTimeField(auto_now=True, verbose_name='Upraveno')
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE, verbose_name='Recept')

    class Hodnoceni(models.IntegerChoices):
        NULA = 0, ''
        JEDNA = 1, '*'
        DVA = 2, '**'
        TRI = 3, '***'
        CTYRI = 4, '****'
        PET = 5, '*****'

    hodnoceni = models.IntegerField(
        default=3,
        choices=Hodnoceni.choices,
        verbose_name='Hodnocení',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        ordering = ['-hodnoceni']
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        return f'{self.text[:30]}..., hodnocení: {self.hodnoceni}'

