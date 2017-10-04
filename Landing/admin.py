# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Submision, member

@admin.register(Submision, member)
class LandingAdmin(admin.ModelAdmin):
    pass