
hostname = "SW1"
management_ip = "192.168.10.2"
vlan_id = 10
cpu_usage = 68.5
ssh_enabled = True

print(hostname)
print(management_ip)
print(vlan_id)
print(cpu_usage)
print(ssh_enabled)

print(type(hostname))
print(type(management_ip))
print(type(vlan_id))
print(type(cpu_usage))
print(type(ssh_enabled))

vlan_id = str(vlan_id)
print(type(vlan_id))