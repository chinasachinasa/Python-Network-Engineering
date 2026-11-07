
packet_loss = 8

if packet_loss == 0:
    print("Network is healthy")

elif packet_loss > 0 and packet_loss < 5:
    print("Minor packet loss")

elif packet_loss >= 5 and packet_loss <= 10:
    print("Warning: High packet loss")

else:
    print("Critical: Network performance degraded")



ssh_available = False
console_available = True

if ssh_available or console_available:
    print("Device accessible")
else:
    print("Device unreachable")






device_online = False
if not device_online:
    print("Device is offline")
else:
    print("Device is online")





#MINI PROJECT: Network Status Checker


device_name = "BR2-SW1"
device_online = True
ssh_available = True
packet_loss = 8


if device_online:
    print("Device is ONLINE")
else:
    print("Device is OFFLINE")


if ssh_available:
    print("SSH: AVAILABLE")
else:
    print("SSH: UNAVAILABLE")



if packet_loss == 0:
    print("NORMAL")
elif packet_loss > 0 and packet_loss < 5:
    print("MINOR")
elif packet_loss >= 5 and packet_loss <= 10:
    print("WARNING")
else:
    print("CRITICAL")




device_name = "BR2-SW1"

print(f"Device: {device_name}")

device_name = "BR2-SW2"

print(f"Device: {device_name}")





print("===========================")
print("NETWORK DEVICE HEALTH REPORT")
print("===========================")
print(f"Device: {device_name}")


print(32*"=")
print("Network Status: ONLINE")
print("SSH Status: AVAILABLE")
print(32*"=")