# raspberry-pi-ozobot-evo
Control your [Ozobot Evo](https://amzn.to/2D91W3s)* with your Raspberry Pi via Bluetooth

Ozobot Evo is a toy robot that has multiple features like automatic path following, remote control via App, proximity sensors, and LEDs.
In this repo you find the code to control the [Ozobot Evo](https://amzn.to/2D91W3s)* with a Raspberry Pi. 


## Special characteristics of the Ozobot Evo protocol
### MAC address
The Ozobot Evo uses different MAC-addresses at each start. In order to connect to the right Bluetooth devivce, you ahve to identify it by name. The names of the Ozobot Evo devices always start with "OzoEvo" followed by an integer

### The StopFile command
In order to be able to send commands to the OzoBot after having connected to it, you have to send an initial stop file command. Only if you do that, the Ozobot will react to the commands that are sent to it. The stop file commnd consists of thre bytes with the hex values 50, 02, 01
```
bot1.c.write(b"\x50\x02\x01")
```
### Bluetooth characteristics
The Ozobot offers two different characteristics. One is only for drive commands, the other for all other types of commands.
```
TRANSMIT_UUID_DRIVE = "8903136c-5f13-4548-a885-c58779136702"
TRANSMIT_UUID_CONTROL = "8903136c-5f13-4548-a885-c58779136703"
```

### Command byte arrays
The format of the byte arrays differs in length based on the command. It always starts with an identifier of the command itself (e.g. 64 for drive and 68 for led), followed by the actual payload.

In many cases, some of the parameters are added twice to the paylod, whereas one of the values is shifted by 8 bits.


* Affiliate Links
