from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date_format(date):
    try:
        datetime.strptime(str(date), "%Y-%m-%d")
    except ValueError:
        raise ValidationError("A data deve estar no formato AAAA-MM-DD")


def validate_title(title):
    separated_title = title.split()
    if len(separated_title) <= 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
