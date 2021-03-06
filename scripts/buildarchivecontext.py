#!/usr/bin/env python
import unittest
import os
from os import path, getenv
from os.path import expanduser
import logging # https://docs.python.org/2/library/logging.html#logging-levels
import glob
import argparse
import sys
import csv
from time import gmtime, strftime

sys.path.append( os.getcwd() ) 
sys.path.insert( 1, 'lib' ) #Pickup libs, rdflib etc., from shipped lib directory
# Ensure that the google.appengine.* packages are available
# in tests as well as all bundled third-party packages.

sdk_path = getenv('APP_ENGINE',  expanduser("~") + '/google-cloud-sdk/platform/google_appengine/')
sys.path.insert(0, sdk_path) # add AppEngine SDK to path

import dev_appserver
dev_appserver.fix_sys_path()

from testharness import *
#Setup testharness state BEFORE importing sdo libraries
setInTestHarness(True)

from api import *
import rdflib
from rdflib import Graph
from rdflib.term import URIRef, Literal
from rdflib.parser import Parser
from rdflib.serializer import Serializer
from rdflib.plugins.sparql import prepareQuery
from rdflib.compare import graph_diff
from rdflib.namespace import RDFS, RDF
import threading

os.environ["WARMUPSTATE"] = "off"
from sdoapp import *
from sdoapp import SCHEMA_VERSION, ALL_LAYERS


from api import GetJsonLdContext

parser = argparse.ArgumentParser()
parser.add_argument("-o","--output", required=True, help="output file")
parser.add_argument("-d","--outputDirectory", default=".",help="output directory - default '.'")
args = parser.parse_args()


ret = GetJsonLdContext(layers=ALL_LAYERS)
fname = "%s/%s" % (args.outputDirectory,args.output)
print("Writing context to: %s" % fname)
file = open(fname, "w")
file.write(ret)
file.close()

