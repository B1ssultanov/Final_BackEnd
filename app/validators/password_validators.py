from django.core.exceptions import ValidationError
import re


def validate_password_strength(password):
    errors = []
    if len(password) < 8:
        errors.append('Password must be at least 8 characters long.')
    if not re.search('[A-Z]', password):
        errors.append('Password must contain at least one uppercase letter.')
    if not re.search('[a-z]', password):
        errors.append('Password must contain at least one lowercase letter.')
    if not re.search('[0-9]', password):
        errors.append('Password must contain at least one number.')
    if errors:
        raise ValidationError(errors)
