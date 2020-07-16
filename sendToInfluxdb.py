import requests
import json
import os
import argparse
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError

script_response = os.popen("speedtest-cli --json").read()

#windows command
#script_response = os.popen("C:\\Users\\marty\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\Scripts\\speedtest-cli --json").read()

parser = argparse.ArgumentParser(description='Gimme')
parser.add_argument('-s', '--influxdbhost', required=True, help='Influxdb host')
parser.add_argument('-P', '--influxdbport', default=8086, help='Influxdb port')
parser.add_argument('-u', '--influxdbusername', required=True, help='Influxdb username')
parser.add_argument('-p', '--influxdbpass', required=True, help='Influxdb pass')
parser.add_argument('-d', '--influxdbdatabase', default="speedtest", help='Influxdb database name')
#parser.add_argument('-j', '--jsondata', required=True, help='Data to send to Influxdb')
args = parser.parse_args()

#convert string to json object
json_full_data = json.loads(script_response)
json_speed_data = json_full_data
name=json_full_data["client"]["ip"]
json_speed_data.pop("client", None)
json_speed_data.pop("server", None)

#--------------------------------------------------------
#post data to influxdb
#--------------------------------------------------------
json_body = [
            {
                "measurement": "speedtestdata",
                "tags": 
                {
                    "name":name
                },
                "fields": json_speed_data
            }
            ]

client = InfluxDBClient(host=args.influxdbhost, port=args.influxdbport, username=args.influxdbusername, password=args.influxdbpass,database=args.influxdbdatabase)

try:
        response = client.write_points(json_body)
        print("Client responded with: ", response)
except InfluxDBClientError as e:
        print(e.content)