device_name = "BR1-SW1"

total_devices = 50
connected_devices = 45
minimum_required = 40

switch_online = True
ssh_enabled = True
telnet_enabled = False

device_available = switch_online
connectivity_ok = connected_devices >= minimum_required
secure_access = ssh_enabled and (not telnet_enabled)
network_healthy = device_available and connectivity_ok and secure_access

print("Device Name:", device_name)
print("Device Available:", device_available)
print("Connectivity OK:", connectivity_ok)
print("Secure Access:", secure_access)
print("Network Healthy:", network_healthy)




device_name = "BR2-SW1"

total_devices = 80
connected_devices = 72
minimum_required = 65

switch_online = True
ssh_enabled = True
telnet_enabled = False

device_available = switch_online

connectivity_ok = connected_devices >= minimum_required

secure_access = ssh_enabled and (not telnet_enabled)

network_healthy = device_available and connectivity_ok and secure_access

print("Device Name:", device_name)
print("Device Available:", device_available)
print("Connectivity OK:", connectivity_ok)
print("Secure Access:", secure_access)
print("Network Healthy:", network_healthy)
