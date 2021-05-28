# AutomatedWifiHacker
Script to automatically navigate terminals and commands for hacking a local AP given the connected MAC of a client, AP Name, Channel, and AP MAC

# This project serves as a medium to understand WiFi hacking, not to present a robust or streamlined solution. If you wish to simply "hack away", other tools like WiFite are better options.

In this script, standard aircrack-ng tools are used (these can be found at https://github.com/aircrack-ng/aircrack-ng).

Info Needed:
MAC address of PC running aircrack-ng suite: 00:0F:B5:88:AC:82 (Sample)
MAC address of the wireless client using WPA2: 00:0F:B5:FD:FB:C2 (Sample)
BSSID (MAC address of access point): 00:14:6C:7E:40:80 (Sample)
ESSID (Wireless network name)
Access point channel
Wireless interface supporting monitor mode

You should gather the equivalent information for the network you will be working on. Without these values, one of more features of the script will not run. 


