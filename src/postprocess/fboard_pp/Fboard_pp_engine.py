#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:49:30 2018

@author: Johanna
"""

from engine.FboardAdapter import FboardAdapter
import time


if __name__ == "__main__":

    try:
        # Creating a CityManager for turin with the coordinates of a NW point
        # and of a SE point, it will be composed of 4*4 Neighborhood and the
        # threshold of open umbrellas per neighborhood after which a rain
        # warning is sent is set to 2
        TurinFboard = FboardAdapter("Turin")
        TurinFboard.process()
        #TurinFboard.myPyPPEMqttClient.mySubscribe("/Turin/notifications/#")
        #Subscriber will be implemented later

        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        TurinFboard.rest()