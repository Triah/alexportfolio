from django.db import models


class Skill(models.Model):
    skill_mastered = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_mastered

class Software(models.Model):
    software_mastered = models.CharField(max_length=200)

    def __str__(self):
        return self.software_mastered