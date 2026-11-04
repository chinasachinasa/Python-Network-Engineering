devices = 10
new_devices = 5
total_devices = devices + new_devices
print(total_devices)


devices1 = 10
group_size = 3
remainder = devices1 % group_size
print(remainder)


borrowed_bits = 3
number_of_subnets = 2 ** borrowed_bits
print(number_of_subnets)


cables = 20
departments = 4
cables_per_department = cables // departments
print(cables_per_department)

print(10==20)
print(10==10)

print(10!=20)
print(10!=10)

print(20>10)
print(5>10)

print(10>=10)
print(15>=10)
print(5>=10)

print(10<=10)
print(5<=10)
print(15<=10)

connected_devices = 45
print(connected_devices > 50 and connected_devices < 100)
print(connected_devices > 30)

vlan_id = 20
print(vlan_id == 10)


device_powered_on = True
ssh_enabled = False
print(device_powered_on and ssh_enabled)

primary_connection = True
backup_connection = False

print(primary_connection or backup_connection)

ssh_enabled1 = True
print(not ssh_enabled1)

device_online = True
ssh_enabled = True
telnet_enabled = False
secure_access = device_online and ssh_enabled and not telnet_enabled

print(secure_access)


total_devices = 50
connected_devices = 45
minimum_required = 40
switch_online = True
telnet_enabled = False

print(total_devices > minimum_required and connected_devices > minimum_required)
print(connected_devices >= minimum_required)
print(connected_devices >= minimum_required and switch_online and not telnet_enabled)

network_healthy = connected_devices >= minimum_required and switch_online
print(network_healthy)

result=10+5*2
print(result)

result=(10+5)*2
print(result)