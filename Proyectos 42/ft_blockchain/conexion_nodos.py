
# Librerias
import json
import requests
import os
from flask import Flask, request

app = Flask(__name__)

def load_node_json(node_json):
    with open(node_json, 'r') as file:
        json_data_node_1 = json.load(file)
        print(type(json_data_node_1))
    return json_data_node_1
    # Make a POST request with the JSON data
    
# Conectamos los 3 nodos y cargamos los archivos json
if __name__ == '__main__':

    url_node1 = 'http://127.0.0.1:5001/connect_node'
    url_node2 = 'http://127.0.0.1:5002/connect_node'
    url_node3 = 'http://127.0.0.1:5003/connect_node'
 
    data1 = load_node_json(node_json='nodo5001.json')
    data2 = load_node_json(node_json='nodo5002.json')
    data3 = load_node_json(node_json='nodo5003.json')

    print(data1,data2,data3)

    headers = {'Content-Type': 'application/json'}
    response1 = requests.post(url=url_node1, json=data1,headers=headers)
    response2 = requests.post(url=url_node2, json=data2,headers=headers)
    response3 = requests.post(url=url_node3, json=data3,headers=headers)

    print(response1.text)
    print(response2.text)
    print(response3.text)
    # app.run(host='0.0.0.0', port='5004',debug=True)
