# RaspberryThermal
Using raspberry to print shopping list or similar to a thermal printer

The idea came from the top of my head just after I connected the thermal printer to my raspberry following these instructions (https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi?view=all) and after a tried this project https://github.com/LukePrior/Raspberry-Pi-Thermal-Printer

The project is simple:
1) Raspberry Pi + Thermal printer
2) Webpage to manage the shopping list of the family

We start from the bullet 2 (see the link above for the setup of the thermal)

We need 2 services 
a) The printer manager that opens a socket and wait for a connection 
b) The service who manage the list on the webpage and send to the first service

...and the webpage
