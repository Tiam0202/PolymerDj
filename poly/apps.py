# coding=utf-8
from django.apps import AppConfig


class PolyConfig(AppConfig):

    name = 'poly'

    def check_models_ready(self):
        return super(PolyConfig, self).check_models_ready()
