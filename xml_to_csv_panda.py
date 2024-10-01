import xml.etree.ElementTree as ET
import pandas as pd

# Define the XML file name
xml_file = 'Export.xml'

# Parse the XML file
xmlparse = ET.parse(xml_file)
root = xmlparse.getroot()

# Prepare a list to hold the data
rows = []

# Loop through each 'articlessql' element in the XML
for article in root.findall('{http://tempuri.org/DataSet1.xsd}articlessql'):
    row = {
        "id": article.find('{http://tempuri.org/DataSet1.xsd}id').text,
        "id_WF": article.find('{http://tempuri.org/DataSet1.xsd}id_WF').text,
        "type_WF": article.find('{http://tempuri.org/DataSet1.xsd}type_WF').text,
        "name": article.find('{http://tempuri.org/DataSet1.xsd}name').text,
        "quantity": article.find('{http://tempuri.org/DataSet1.xsd}quantity').text,
        "sell_price": article.find('{http://tempuri.org/DataSet1.xsd}sell_price').text,
        "sellid": article.find('{http://tempuri.org/DataSet1.xsd}sellid').text,
        "whole_price": article.find('{http://tempuri.org/DataSet1.xsd}whole_price').text,
        "group": article.find('{http://tempuri.org/DataSet1.xsd}group').text,
        "barcode": article.find('{http://tempuri.org/DataSet1.xsd}barcode').text,
        "measure": article.find('{http://tempuri.org/DataSet1.xsd}measure').text,
        "nnumber": article.find('{http://tempuri.org/DataSet1.xsd}nnumber').text,
    }
    rows.append(row)

# Create a DataFrame from the rows
df = pd.DataFrame(rows)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)