from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

class Quiz(models.Model):
    nombre = models.CharField(max_length=70, verbose_name='Prueba:', null=False)
    description = models.CharField(max_length=100, verbose_name='Descripción:', default='Preguntas Básicas')
    slug = models.SlugField(blank=True, verbose_name='enlace:')
    roll_out = models.BooleanField(default=False, verbose_name='¿Desenrollar?')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación:')

    class Meta:
        ordering = ['timestamp',]
        verbose_name_plural = 'Quizzes'
    
    def __str__(self) -> str:
        return self.nombre

class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, null=False, verbose_name='etiqueta:')
    order = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.label

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, verbose_name='etiqueta')
    is_correct = models.BooleanField(default=False, verbose_name='¿Respuesta Correcta?')

    def __str__(self) -> str:
        return self.label

class QuizTaker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario:')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Prueba:')
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False, verbose_name='¿Completado?')
    date_finishied = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email

class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.question.label

@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.nombre)