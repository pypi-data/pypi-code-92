from firstimpression.constants import APIS, TEMP_FOLDER, LOCAL_INTEGRATED_FOLDER
from firstimpression.api.request import request
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.scala import variables
import xml.etree.ElementTree as ET
import os
import glob

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['solaredge']
URL = 'https://monitoringpublic.solaredge.com/solaredge-web/p/kiosk/kioskData?locale=nl_NL'

XML_TEMP_PATH = os.path.join(TEMP_FOLDER, NAME, 'data.xml')
XML_LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, 'data*.xml')

MAX_FILE_AGE = 60 * 5



##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(guid):

    update_directories_api(NAME)

    if check_too_old(XML_TEMP_PATH, MAX_FILE_AGE):

        root = ET.Element("root")

        response = request(URL, params={'guid':guid}, method='post').text.split('\n')

        co2_saved = ''
        trees_saved = ''
        last_day_energy = ''

        for elem in response:
            if 'CO2EmissionSaved' in elem:
                co2_saved = '{:,}'.format(int(round(float(elem.split(':')[1].split(' ')[0][1:].replace('.', '').replace(',','.')),0))).replace(',', '.') + ' kg'
            if 'treesEquivalentSaved' in elem:
                trees_saved = '{:,}'.format(int(round(float(elem.split(':')[1][1:-3].replace('.', '').replace(',','.')),0))).replace(',', '.')
            if 'lastDayEnergy' in elem:
                last_day_energy = elem.split(':')[1][1:-3]

        ET.SubElement(root, "EmissionSaved").text = co2_saved
        ET.SubElement(root, "TreesSaved").text = trees_saved
        ET.SubElement(root, "EnergyToday").text = last_day_energy

        write_root_to_xml_files(root, XML_TEMP_PATH, NAME)

def check_api():
    svars = variables()

    file_path = glob.glob(XML_LOCAL_PATH)

    if len(file_path) > 0:
        file_path = file_path[0]    
        if check_too_old(file_path, MAX_FILE_AGE):
            svars['skipscript'] = True
        else:
            svars['skipscript'] = False
    else:
        svars['skipscript'] = True

    


##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################


##################################################################################################
# PARSE FUNCTIONS
##################################################################################################