import uuid

from django.db import models


class Expedition(models.Model):
    STATUT_CHOICES = [
        ("publiee", "Publiée"),
        ("attribuee", "Attribuée"),
        ("en_cours", "En cours"),
        ("livree", "Livrée"),
        ("annulee", "Annulée"),
    ]

    reference = models.CharField(max_length=20, unique=True, editable=False)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    date_souhaitee = models.DateField()
    poids_kg = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="publiee",
    )
    entreprise = models.ForeignKey(
        "EntreprisesApp.Entreprise",
        on_delete=models.CASCADE,
        related_name="expeditions",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f"EXP-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} ({self.ville_depart} → {self.ville_arrivee})"
