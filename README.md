Projecto para leer, procesar y analizar telemetria asi como digitalizar instrumentos a traves del puerto OBD2
escrito en python3 ejecutado directamente en ALpine Linux y Docker.
##################################################################
Install Python and Necessary Packages
Install Python: Alpine uses apk for package management. Install Python if it’s not already installed:

apk add python3 py3-pip
Install python-OBD: This library helps in interfacing with the OBD-II port.

pip3 install python-OBD

Install Additional Packages (if necessary):

You may need to install additional packages for your OBD-II adapter, like pyserial if you're using a serial connection.

pip3 install pyserial

Connect to OBD2 port and run
