from . import BaseCommand


class Command(BaseCommand):
    args = "<TEMPLATE_PATH>"

    def handle(self, block_name, template_path, *args, **options):
        raise NotImplemented()
