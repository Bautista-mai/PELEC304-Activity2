from django.db import models

class Student(models.Model):
    stud_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    course = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".replace("  ", " ")


class StudentBackground(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='background')
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=20, blank=True)
    elementary_school = models.CharField(max_length=150, blank=True)
    high_school = models.CharField(max_length=150, blank=True)
    previous_school = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Background of {self.student}"