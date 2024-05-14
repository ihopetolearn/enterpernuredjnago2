from django.core.exceptions import ValidationError

valid_unit_measurements = ["pound", "lbs", "oz", "grams"]



def vlidation_unit_measure(value):
    if value not in valid_unit_measurements:
        raise ValidationError(f"{value} is not in the list")