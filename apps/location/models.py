from django.db import models
from django.conf import settings

class Location(models.Model):
    # Ustaxonani qaysi usta kiritganini bog'lash
    usta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Ustaxonaning asosiy ma'lumotlari
    nomi = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200) # Masalan: "Chilonzor 3-kvartal, Mo'ljal: Makro"
    
    # Xizmat turlarini oddiy matn qilib saqlaymiz
    xizmatlar = models.TextField(help_text="Qanday xizmatlar borligini yozing (masalan: Motor, Moy, Balon)")
    
    def __str__(self):
        return self.nomi
