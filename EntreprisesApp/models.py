from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid


class UtilisateurManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email obligatoire")
        email = self.normalize_email(email)
        if 'user_id' not in extra_fields:
            extra_fields['user_id'] = uuid.uuid4().hex[:8].upper()
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        return self.create_user(username, email, password, **extra_fields)


class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('chargeur', 'chargeur'), ('transporteur', 'transporteur'), ('admin', 'admin')], default='chargeur')
    telephone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UtilisateurManager()


class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=255)
    matricule_fiscal = models.CharField(max_length=17, unique=True)
    type_entreprise = models.CharField(max_length=15, choices=[('chargeur', 'chargeur'), ('transporteur', 'transporteur')])
    adresse = models.TextField()
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
