from django.core.files.images import get_image_dimensions
from django.conf import settings


def validate_cover(value):
    size = get_image_dimensions(value)
    if size > settings.MAX_UPLOAD_ADMIN_SIZE:
        raise ValueError("Please keep file size under 2 MB")