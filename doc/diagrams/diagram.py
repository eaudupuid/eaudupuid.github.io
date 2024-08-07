from diagrams import Diagram
from diagrams.aws.compute import *
from diagrams.aws.management import *
from diagrams.aws.database import *
from diagrams.aws.network import *
from diagrams.aws.iot import *
from diagrams.aws.general import *
from diagrams.aws.migration import *


with Diagram("transmission et stockage des donnees de captage", show=False):
    (
        IotAlexaEnabledDevice("capteur EauDuPuid")
        >> IotOverTheAirUpdate("reseau GSM")
        >> IotMqtt("mqtt protocol")
        >> Cloudtrail("cloud")
        >> InternetAlt1("logiciel EauDuPuid")
        >> GenericDatabase("base de donnees")
        >> Client("ordinateur")
        >> User("Mairie")
        >> TraditionalServer("Rapport")
    )
