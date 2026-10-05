from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    """
    Represents a technical or professional skill with a proficiency percentage.
    """
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    level = models.CharField(max_length=50, default="Intermediate", verbose_name=_("Level")) 
    category = models.CharField(max_length=100, default="General", verbose_name=_("Category"))  
    description = models.TextField(default="No description provided.", verbose_name=_("Description"))
    proficiency = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_("Proficiency")
    )
    
    class Meta:
        ordering = ['name']
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return f"Skill: {self.name}"


class Project(models.Model):
    """
    Represents a portfolio project with a description, link, image, and related skills.
    """
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name=_("Slug"))
    description = models.TextField(verbose_name=_("Description"))
    category = models.CharField(max_length=100, default="General", verbose_name=_("Category"))
    link = models.URLField(blank=True, null=True, verbose_name=_("Link"))
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name=_("Image"))
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True, verbose_name=_("Skills"))
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created At"))

    class Meta:
        ordering = ['title']
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f"Project: {self.title}"
