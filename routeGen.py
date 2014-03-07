#!/usr/bin/env python
"""
@file    runner.py
@author  Lena Kalleske
@author  Daniel Krajzewicz
@author  Michael Behrisch
@date    2009-03-26
@version $Id: runner.py 14678 2013-09-11 08:53:06Z behrisch $

Route generation script.

SUMO, Simulation of Urban MObility; see http://sumo.sourceforge.net/
Copyright (C) 2009-2012 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import os, sys
import optparse
import subprocess
import random

def generate_routefile():
    random.seed(41) # make tests reproducible
    N = 3600 # number of time steps
    # demand per second from different directions
    pRD = 1./10 		#right-down road
    pLL = 1./11			#Left-left road
    pDL = 1./12			#Down-low road
    pDR = 1./30			#Down-right road
    pDD = 1./1			#Down-down road
    with open("cross.rou.xml", "w") as routes:
        print >> routes, """<routes>
        <vType id="typePassenger" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>
        <vType id="typeBus" accel="0.8" decel="4.5" sigma="0.5" length="10" minGap="3" maxSpeed="25" guiShape="bus"/>

        <route id="right-down" edges="2i 3o" />
        <route id="left-left"  edges="2i 1o" />
        <route id="down-left"  edges="4i 1o" />
        <route id="down-right" edges="4i 2o" />
        <route id="down-down"  edges="4i 3o" />"""
        lastVeh = 0
        vehNr = 0
        for i in range(N):
            if random.uniform(0,1) < pRD:
                print >> routes, '    <vehicle id="%i" type="typeBus" route="right-down" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            if random.uniform(0,1) < pLL:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="left-left" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            if random.uniform(0,1) < pDL:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="down-left" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            if random.uniform(0,1) < pDR:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="down-right" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            if random.uniform(0,1) <= pDD:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="down-down" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            print ("pDD: %f, pDR: %f") %(pDD, pDR)
            print ("random.uniform(0,1): %f") %(random.uniform(0,1))
        print >> routes, "</routes>"

# this is the main entry point of this script
if __name__ == "__main__":
    
    generate_routefile()
