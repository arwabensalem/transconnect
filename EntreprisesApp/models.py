import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UtilisateurManager(BaseUserManager):
    """Manager personnalisé pour générer user_id à la création."""

    def _generate_user_id(self):
        while True:
            user_id = uuid.uuid4().hex[:8].upper()
            if not self.model.objects.filter(user_id=user_id).exists():
                return user_id

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire.")
        email = self.normalize_email(email)
        extra_fields.setdefault("user_id", self._generate_user_id())
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Le superutilisateur doit avoir is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Le superutilisateur doit avoir is_superuser=True.")
        return self.create_user(username, email, password, **extra_fields)


class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ("chargeur", "Chargeur"),
        ("transporteur", "Transporteur"),
        ("admin", "Administrateur"),
    ]

    user_id = models.CharField(max_length=8, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="chargeur")
    telephone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UtilisateurManager()

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = Utilisateur.objects._generate_user_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Entreprise(models.Model):
    TYPE_CHOICES = [
        ("chargeur", "Chargeur"),
        ("transporteur", "Transporteur"),
    ]

    raison_sociale = models.CharField(max_length=255)
    matricule_fiscal = models.CharField(max_length=17, unique=True)
    type_entreprise = models.CharField(max_length=15, choices=TYPE_CHOICES)
    adresse = models.TextField()
    utilisateur = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name="entreprise",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.raison_sociale
