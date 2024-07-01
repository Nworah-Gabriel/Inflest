from django.core.management.base import BaseCommand
# from scripts.import_data import import_data
from .scripts.import_data import import_data
class Command(BaseCommand):
    help = 'Import macroeconomic data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        import_data(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
