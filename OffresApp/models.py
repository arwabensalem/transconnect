from django.db import models

from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule


class Offre(models.Model):
    STATUT_CHOICES = [
        ("proposee", "Proposée"),
        ("acceptee", "Acceptée"),
        ("refusee", "Refusée"),
        ("retiree", "Retirée"),
    ]

    prix = models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="proposee",
    )
    date_proposition = models.DateField(auto_now_add=True)
    expedition = models.ForeignKey(
        Expedition,
        on_delete=models.CASCADE,
        related_name="offres",
    )
    transporteur = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name="offres_proposees",
    )
    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE,
        related_name="offres",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Offre {self.prix}€ — {self.expedition.reference}"
