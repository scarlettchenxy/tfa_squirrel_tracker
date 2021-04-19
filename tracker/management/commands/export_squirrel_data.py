from django.core.management.base import BaseCommand

from ...utils import write_export_data


class Command(BaseCommand):
    help =  'export squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        import_file_name = options['filename'][0]
        write_export_data(import_file_name)
