from . import BaseCommand


class Command(BaseCommand):
    args = "<BLOCK_NAME> <TEMPLATE_PATH>"

    def handle(self, block_name, template_path, *args, **options):
        pass
