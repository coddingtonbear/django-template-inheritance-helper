import os.path

from django.core.management.base import BaseCommand as DjangoBaseCommand
from django.template import Template


class BaseCommand(DjangoBaseCommand):
    def get_template(self, path):
        real_path = os.path.expanduser(path)
        with open(real_path, 'r') as infile:
            return Template(infile.read())
