# RaspberryThermal
Using raspberry to print shopping list or similar to a thermal printer

The idea came from the top of my head just after I connected the thermal printer to my raspberry following these instructions (https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi?view=all) and after a tried this project https://github.com/LukePrior/Raspberry-Pi-Thermal-Printer

The project is simple:
1) Raspberry Pi + Thermal printer
2) Webpage to manage the shopping list of the family

We start from the bullet 2 (see the link above for the setup of the thermal)

We need 2 services 
a) The printer manager that opens a socket and wait for a connection (file printerManager.py)
b) The service who manage the list on the webpage and send to the first service (file server.py) (or setup it with a standar Apache, ngnix, .... if already you have one)

...and the webpage (index.html)

![ShoppingList](https://github.com/user-attachments/assets/e1ef263b-2381-4b47-9d55-854a09bfe846)


Then we setup the two service to start at the boot

# Service 1 - Printer 
>sudo nano /etc/systemd/system/printerManager.service

content of file

>[Unit]
>Description=Thermal printer manager
>After=network.target
>
>[Service]
>User=pi
>
>WorkingDirectory=/home/pi/printerManager
>
>ExecStart=/usr/bin/python3 /home/pi/printerManager/printerManager.py
>
>Restart=always
>
>[Install]
>WantedBy=multi-user.target


and then

>sudo systemctl daemon-reload
>
>sudo systemctl restart printerManager.service
>
>sudo systemctl status printerManager.service

For the other service we do de same

# Service 2 - Server
>sudo nano /etc/systemd/system/httpServer.service

content of file
>[Unit]
>Description=Server HTTP for Shopping List
>After=network.target
>
>[Service]
>User=pi
>
>WorkingDirectory=/home/pi/httpServer
>
>ExecStart=/usr/bin/python3 /home/pi/printerManager/server.py
>
>Restart=always
>
>[Install]
>WantedBy=multi-user.target


and then

comand line
>sudo systemctl daemon-reload
>
>sudo systemctl restart httpServer.service
>
>sudo systemctl status httpServer.service

You can now test connexcting to the desired webpage address and trying to print something.

>[!NOTE]
>
>Webpage: you can drag the elements to order the list (https://github.com/SortableJS/Sortable), mark or unmark them.
>"memory" file (named save in the same directory of the index.html



