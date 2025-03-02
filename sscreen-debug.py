#!/usr/bin/python3
import sys
import csv
import json
import xml.etree.ElementTree as ET
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view

def parse_smartscreen_evtx(evtx_file_path, output_csv):
    with open(evtx_file_path, 'rb') as evtx_file:
        evtx_data = evtx_file.read()
    file_header = FileHeader(evtx_data, 0)
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Computer Name', 'UserID', 'Record Time', 'Path', 'Execution Time'])
        for xml, record in evtx_file_xml_view(file_header):
            try:
                event = ET.fromstring(xml)
                namespaces = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}
                system = event.find('ns:System', namespaces)
                event_data = event.find('ns:EventData', namespaces)
                if event_data is not None:
                    data = event_data.find('ns:Data', namespaces)
                    if data is not None and 'isFileSupported' in data.text:
                        try:
                            data_json = json.loads(data.text)
                            if 'executionTime' in data_json and 'path' in data_json:
                                computer_name = system.find('ns:Computer', namespaces).text
                                user_id = system.find('ns:Security', namespaces).attrib['UserID']
                                time_created = system.find('ns:TimeCreated', namespaces).attrib['SystemTime']
                                path = data_json['path']
                                execution_time = data_json['executionTime']
                                writer.writerow([computer_name, user_id, time_created, path, execution_time])
                        except json.JSONDecodeError:
                            continue
            except ET.ParseError:
                continue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./sscreen-debug.py <evtx_file> <output>.csv")
        sys.exit(1)
    evtx_file_path = sys.argv[1]
    output_csv = sys.argv[2]
    parse_smartscreen_evtx(evtx_file_path, output_csv)