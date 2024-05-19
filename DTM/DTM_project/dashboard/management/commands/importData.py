# myapp/management/commands/import_data.py

import pandas as pd
from django.core.management.base import BaseCommand
from dashboard.models import ThreatData
import os

class Command(BaseCommand):
    help = 'Import data from a JSON file into the ThreatData model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the file with JSON content')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # Check if the file exists
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        try:
            # Read the JSON lines content from the file
            df = pd.read_json(file_path, lines=True)
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f"Failed to read JSON data: {e}"))
            return

        # Define a mapping of model fields to the respective JSON keys
        field_mapping = {
            'classification_taxonomy': 'classification.taxonomy',
            'classification_type': 'classification.type',
            #'event_description': 'event.description',
            'feed_accuracy': 'feed.accuracy',
            'feed_name': 'feed.name',
            'feed_provider': 'feed.provider',
            'feed_url': 'feed.url',
            'protocol_application': 'protocol.application',
            'source_abuse_contact': 'source.abuse_contact',
            #'source_allocated': 'source.allocated', 
            'source_as_name': 'source.as_name',
            'source_asn': 'source.asn',
            'source_geolocation_cc': 'source.geolocation.cc',
            'source_ip': 'source.ip',
            'source_network': 'source.network',
            'source_registry': 'source.registry',
            'time_observation': 'time.observation',
            'time_source': 'time.source',
            'extra_blocklist': 'extra.blocklist',
            'source_fqdn': 'source.fqdn',
            'source_port': 'source.port',
            'source_url': 'source.url',
            'source_urlpath': 'source.urlpath',
            'status': 'status',
            'protocol_transport': 'protocol.transport',
            'malware_name': 'malware.name',
            'source_reverse_dns': 'source.reverse_dns',
        }

        # Import data row by row, considering only relevant columns
        for _, row in df.iterrows():
            # Create a dictionary with valid fields mapped to their respective values
            data = {}
            for field, json_key in field_mapping.items():
                data[field] = row.get(json_key)

            # Convert datetime fields
            data['time_observation'] = pd.to_datetime(data['time_observation'], errors='coerce')
            data['time_source'] = pd.to_datetime(data['time_source'], errors='coerce')

            # Create a new record in the ThreatData model
            try:
                ThreatData.objects.create(**data)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row: {e}"))

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
