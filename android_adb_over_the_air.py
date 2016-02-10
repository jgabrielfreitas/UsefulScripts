from subprocess import call

def connect():
    # $ ./adb tcpip 4455
    phone_ip = "192.168.0.16" # TYPE HERE YOUR DEVICE'S IP AT NETWORK
    call(["./adb", "tcpip", "4455"])

    # $ ./adb connect 192.168.0.16:4455 <-- example
    call(["./adb", "connect", "{0}:4455".format(phone_ip)])


print("Certificate that your device is connected via USB")
is_connected_via_usb = raw_input("Your device is already connected via USB? [S/N]")

if is_connected_via_usb.upper() == 'S':
    connect()
else:
    print("Connect your device and run this script again")
