from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Customer


class Ichimliklar(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField()
    isbn = models.PositiveIntegerField(unique=True)
    image_drink = models.ImageField(default=False, upload_to='media/ichimliklar_image')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    company = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ichimliklarr_table'


class ReviewDrinkModel(models.Model):
    user = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    drink = models.ForeignKey(Ichimliklar, blank=True, null=True, on_delete=models.CASCADE)
    comment_body = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        ]
    )
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


