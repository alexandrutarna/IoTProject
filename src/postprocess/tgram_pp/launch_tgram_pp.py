"""
PostProcess Engine for Telegram:

Main script to be run to make the postprocess engine operational.
It instantiates a CityManager, starts it, subscribes to the notifications topic
and waits until Ctrl+'C' is pressed.
"""

from engine.CityManager import CityManager
import time
import requests
import json
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), \
                                            './../../catalog/')))
from classes import IamAlive
from util import *

if __name__ == "__main__":

    # Loading configuration file
    conf = json.load(open("conf.json", "r"))

    # 1) Perform registration to catalog by creating dedicated thread
    registration(conf)

    # 2) Retrieve information regarding broker
    broker_host, broker_port = getBroker(conf)

    # 3) Ask for information about next actor    

    try:
        # Creating a CityManager for turin with the coordinates of a NW point
        # and of a SE point, it will be composed of 4*4 Neighborhood and the
        # threshold of open umbrellas per neighborhood after which a rain
        # warning is sent is set to 2
        topic = conf["catalog"]["registration"]["expected_payload"] \
                    ["requirements"]["topics"][0]
        confCM = conf["CityManager"]
        coord = confCM["coordinates"]
        TurinManager = CityManager(confCM["name"], broker_host, broker_port, \
                                   coord["nwLat"], coord["nwLong"], \
                                   coord["seLat"], coord["seLong"], \
                                   confCM["n"], confCM["threshold"])
        TurinManager.manage()
        TurinManager.myPyPPEMqttClient.mySubscribe(topic)

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        TurinManager.rest()
