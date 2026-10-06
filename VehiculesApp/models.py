from django.db import models


class Vehicule(models.Model):
    TYPE_VEHICULE_CHOICES = [
        ("camionnette", "Camionnette"),
        ("fourgon", "Fourgon"),
        ("camion_porteur", "Camion porteur"),
        ("semi-remorque", "Semi-remorque"),
    ]

    immatriculation = models.CharField(max_length=20, unique=True)
    type_vehicule = models.CharField(max_length=50, choices=TYPE_VEHICULE_CHOICES)
    capacite_kg = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    entreprise = models.ForeignKey(
        "EntreprisesApp.Entreprise",
        on_delete=models.CASCADE,
        related_name="vehicules",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.immatriculation} ({self.type_vehicule})"
