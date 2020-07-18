import argparse
import xml.etree.ElementTree as ET

# Select whether the ICAO code of the airport should be shown at the beginning of the line
showICAO = True

# Add parsing arguments and parse
parser = argparse.ArgumentParser(description='Downloading and printing airport METAR.')
parser.add_argument('icao', metavar='icao', type=str, nargs='+',
                    help='Airport ICAO')

args = parser.parse_args()

# Loop over all ICAO codes and print the METAR
for x in args.icao:
    import urllib.request

    with urllib.request.urlopen(
            'https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve'
            '&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=10&stationString=' + x) as f:
        html = f.read().decode('utf-8')
        root = ET.fromstring(html)
        string = root.find('data/METAR/raw_text').text
        if showICAO:
            print(string)
        else:
            print(string[5:])
