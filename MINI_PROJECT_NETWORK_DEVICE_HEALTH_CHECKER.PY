

device_name = "BR2-SW1"
device_online = True
ssh_available = True
packet_loss = 8

print("=" * 32)
print("NETWORK DEVICE HEALTH REPORT")
print("=" * 32)
print(f"Device: {device_name}")

if device_online:
    print("Status: ONLINE")
else:
    print("Status: OFFLINE")

if ssh_available:
    print("SSH: AVAILABLE")
else:
    print("SSH: UNAVAILABLE")

print(f"Packet Loss: {packet_loss}%")

if packet_loss == 0:
    print("HEALTHY")
elif packet_loss > 0 and packet_loss < 5:
    print("MINOR")
elif packet_loss >= 5 and packet_loss <= 10:
    print("WARNING")
else:
    print("CRITICAL")

print("=" * 32)
