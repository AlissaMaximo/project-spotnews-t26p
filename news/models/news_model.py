from django.db import models
from news.middlewares import validate_title, validate_date_format


class News(models.Model):
    author = models.ForeignKey("Users", on_delete=models.CASCADE, null=False)
    content = models.TextField(null=False)
    categories = models.ManyToManyField("Categories", null=False)
    image = models.ImageField(upload_to="img/", blank=True)
    created_at = models.DateField(
        null=False, validators=[validate_date_format]
    )
    title = models.CharField(
        null=False, max_length=200, validators=[validate_title]
    )

    def __str__(self):
        return self.title
