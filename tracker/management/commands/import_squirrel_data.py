import os

from django.core.management.base import BaseCommand

from ...utils import write_import_data
from project.settings import BASE_DIR


class Command(BaseCommand):
    help = 'import squirrel data to database'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        filename = options['filename'][0]
        file_path = os.path.join(BASE_DIR,filename)
        write_import_data(file_path)
