from django.db import models

# Model that structures a job posting that an employer would create
class JobPost(models.Model):
    EXPERIENCE_LEVELS = [
        ("Internship", "Internship"),
        ("Entry", "Entry"),
        ("Associate", "Associate"),
        ("Mid-Senior", "Mid-Senior"),
        ("Director", "Director"),
        ("Executive", "Executive"),
    ]

    COMPENSATION_RATES = [
        ("Hourly", "Hourly"),
        ("Yearly", "Yearly"),
    ]

    title = models.CharField(max_length=250)
    company = models.CharField(max_length=100)
    experience_level = models.CharField(choices=EXPERIENCE_LEVELS, max_length=25)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    compensation_quantity = models.DecimalField(decimal_places=2, max_digits=10)
    compensation_rate = models.CharField(choices=COMPENSATION_RATES, max_length=10)

    def __str__(self):
        return self.title

