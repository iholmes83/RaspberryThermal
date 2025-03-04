# RaspberryThermal
Using raspberry to print shopping list or similar to a thermal printer

The idea came from the top of my head just after I connected the thermal printer to my raspberry following these instructions (https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi?view=all) and after a tried this project https://github.com/LukePrior/Raspberry-Pi-Thermal-Printer

The project is simple:
1) Raspberry Pi + Thermal printer
2) Webpage to manage the shopping list of the family

We start from the bullet 2 (see the link above for the setup of the thermal)

We need 2 services 
a) The printer manager that opens a socket and wait for a connection (file printerManager.py)
b) The service who manage the list on the webpage and send to the first service (file server.py)

...and the webpage (index.html)

Then we setup the two service to start at the boot

# Service 1
sudo nano /etc/systemd/system/printerManager.service

content of file

[Unit]
Description=Server HTTP Flask per Lista della Spesa
After=network.target

[Service]
User=hoobs
WorkingDirectory=/home/pi/printerManager
ExecStart=/usr/bin/python3 /home/pi/printerManager/printerManager.py
Restart=always

[Install]
WantedBy=multi-user.target


and then

sudo systemctl daemon-reload
sudo systemctl restart printerManager.service
sudo systemctl status printerManager.service

For the other service we do de same

# Service 2
sudo nano /etc/systemd/system/httpServer.service

content of file
[Unit]
Description=Server HTTP Flask per Lista della Spesa
After=network.target

[Service]
User=hoobs
WorkingDirectory=/home/pi/httpServer
ExecStart=/usr/bin/python3 /home/pi/printerManager/server.py
Restart=always

[Install]
WantedBy=multi-user.target


and then

comand line
sudo systemctl daemon-reload
sudo systemctl restart httpServer.service
sudo systemctl status httpServer.service
