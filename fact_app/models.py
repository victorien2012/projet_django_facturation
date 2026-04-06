from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    SEX_TYPES = (('M', 'Masculin'), ('F', 'Feminin'))
    name = models.CharField(max_length=132)
    email = models.EmailField()
    telephone = models.CharField(max_length=132)
    address = models.CharField(max_length=64)
    sexe = models.CharField(max_length=1, choices=SEX_TYPES)
    age = models.CharField(max_length=12)
    ville = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    date_creation = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class Facture(models.Model):
    FACTURE_TYPES = (
        ('R', 'RECU'),
        ('P', 'FACTURE PROFORMA'),
        ('F', 'FACTURE')
    )
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    facture_date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=20)  # max_digits corrigé
    last_update_date = models.DateTimeField(null=True, blank=True)
    paye = models.BooleanField(default=False)
    facture_type = models.CharField(max_length=1, choices=FACTURE_TYPES)
    ville = models.CharField(max_length=32)
    commentaire = models.TextField(null=True, max_length=1000, blank=True)

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
            # Format : Nom_JJ/MM/AAAA à HH:MM
            return f"Facture de {self.client.name}_{self.facture_date_time.strftime('%d/%m/%Y à %H:%M')}"

    @property
    def get_total(self):
        articles = self.article_set.all()
        # On calcule la somme des totaux de chaque article
        return sum(article.get_total for article in articles)


class Article(models.Model):
    # on_delete=models.CASCADE : si on supprime la facture, on supprime ses articles
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    name = models.CharField(max_length=132)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=20)
    total = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    @property
    def get_total(self):
        # Retourne le calcul réel
        return self.quantity * self.unit_price

    def __str__(self):
        return self.name