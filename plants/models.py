from django.db import models
from django.urls import reverse
from django.utils.text import slugify
 
class Category(models.Model):
    """Categories for plants """

    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)
 
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
 
    def get_absolute_url(self):
        return reverse("plants:category", kwargs={"slug": self.slug})
 
    def __str__(self):
        return self.name
 
 
class Plant(models.Model):
    """Stores plants for sale"""

    # choices 
 
    class Light(models.TextChoices):
        LOW = "low", "Low light"
        MEDIUM = "medium", "Bright indirect"
        HIGH = "high", "Full sun"
 
    class Difficulty(models.TextChoices):
        EASY = "easy", "Easy"
        MODERATE = "moderate", "Moderate"
        HARD = "hard", "Expert"

    class Humidity(models.TextChoices):
        LOW = "low", "Low (dry air is fine)"
        AVERAGE = "average", "Average household"
        HIGH = "high", "High (mist or use a humidifier)"

    # main data fields
 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="plants")
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    scientific_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
 
    # Care info
    light = models.CharField(max_length=10, choices=Light.choices, default=Light.MEDIUM)
    difficulty = models.CharField(max_length=10, choices=Difficulty.choices, default=Difficulty.EASY)
    watering_interval_days = models.PositiveIntegerField(default=7, help_text="Recommended days between watering")
    pet_safe = models.BooleanField(default=False)
    humidity = models.CharField(max_length=10, choices=Humidity.choices, default=Humidity.AVERAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["is_active", "category"])]
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
 
    def get_absolute_url(self):
        return reverse("plants:detail", kwargs={"slug": self.slug})
 
    def __str__(self):
        return self.name
