# -*- coding: utf-8 -*-
from django.conf import settings

def site(request):
    """
    Adds media-related context variables to the context.
    """
    return {'SITE_NAME': settings.SITE_NAME}
