#CONDITIONAL STATEMENTS#

switch_online = True

if switch_online:
    print("Switch is online")
else:
    print("Switch is offline")


#switch_online = False

#if switch_online:
   # print("Switch is online")


router_cpu = 90

if router_cpu > 80:
    print("WARNING: High CPU usage")


switch_name = "CORE-SW1"
switch_online = False

if switch_online:
    print(switch_name, "is online")

#You are monitoring a switch.
#  You do not want your monitoring program
#  to remain silent
#  when the switch goes offline.#


#If the switch is online, display Switch is online
#Otherwise, display ALERT: Switch is offline.#

switch_online = False

if switch_online:
    print("Switch is online")
else:
    print("ALERT: Switch is offline")


switch_online = True

if switch_online:
    print("Switch is online")
else:
    print("ALERT: Switch is offline")




cpu_usage = 75

if cpu_usage > 80:
    print("WARNING: High CPU usage")

elif cpu_usage > 60:
    print("NOTICE: Moderate CPU usage")

else:
    print("CPU usage is normal")





cpu_usage1 = 65
if cpu_usage1 > 80:
    print("WARNING: High CPU usage.")
elif cpu_usage1 > 60:
    print("NOTICE: Moderate CPU usage.")
else:
    print("CPU usage is normal.")



cpu_usage2 = 90
if cpu_usage2 > 80:
    print("WARNING: High CPU usage.")
elif cpu_usage2 > 60:
    print("NOTICE: Moderate CPU usage.")
else:
    print("CPU usage is normal.")




cpu_usage3 = 40
if cpu_usage3 > 80:
    print("WARNING: High CPU usage.")
elif cpu_usage3 > 60:
    print("NOTICE: Moderate CPU usage.")
else:
    print("CPU usage is normal.")



router_online1 = True
cpu_usage4 = 90

if router_online1 and cpu_usage4 > 80:
    print("ALERT: Router is online but CPU usage is critically high")





switch_online6 = False
ssh_enabled = True

if switch_online6 and ssh_enabled:
    print("Switch is online and SSH is enabled")

else:
    print("WARNING: Check switch connectivity or SSH")




cpu_usage5 = 70
memory_usage = 95
if cpu_usage5 > 80 or memory_usage > 90:
    print("ALERT: High resource usage detected")
else:
    print("Resource usage is normal")





is_switch_offline = True
is_ssh_disabled = False

if is_switch_offline or is_ssh_disabled:
    print("SECURITY ALERT: Check switch availability or SSH configuration")
else:
    print("Switch is online and SSH is enabled.")



is_switch_offline1 = False
is_ssh_disabled = False

if is_switch_offline1 or is_ssh_disabled:
    print("SECURITY ALERT: Check switch availability or SSH configuration")
else:
    print("Switch is online and SSH is enabled.")



is_switch_offline2 = False
is_ssh_disabled = True

if is_switch_offline2 or is_ssh_disabled:
    print("SECURITY ALERT: Check switch availability or SSH configuration")
else:
    print("Switch is online and SSH is enabled.")



router_online8 = True
cpu_usage8 = 90
ssh_enabled8 = True

(router_online8 and cpu_usage8 > 80) or not ssh_enabled8





router_online9 = False
cpu_usage9 = 50
ssh_enabled9 = False

if (router_online9 and cpu_usage9 > 80) or not ssh_enabled9:
    print("SECURITY ALERT: Investigate router security")

else:
    print("Router security status is normal")




interface_up = False

if not interface_up:
    print("ALERT: Interface is down")
else:
    print("Interface is operational")



router_online11 = False

if not router_online11:
    print("ALERT: Router is offline")
else:
    print("Router is online")



firewall_enabled11 = True

if not firewall_enabled11:
    print("WARNING: Firewall is disabled")
else:
    print("Firewall is enabled")




router_online12 = True
ssh_enabled12 = False
firewall_enabled12 = True

if router_online12 and not ssh_enabled12 or not firewall_enabled12:
    print("SECURITY ALERT: Check network security")
else:
    print("Network security is normal")



router_online13 = False
ssh_enabled13 = True
firewall_enabled13 = False

if not router_online13 or not ssh_enabled13:
    print("ALERT: Network connectivity or SSH problem")

elif not firewall_enabled13:
    print("WARNING: Firewall is disabled")

else:
    print("Network is secure and operational")






router_online14 = True
cpu_usage14 = 85
ssh_enabled14 = False

if not router_online14:
    print("CRITICAL: Router is offline")

elif cpu_usage14 > 80:
    print("WARNING: High CPU usage")

elif not ssh_enabled14 :
    print("SECURITY ALERT: SSH is disabled")

else:
    print("Network device is healthy")






router_online15 = False
cpu_usage15 = 45
ssh_enabled15 = False

if not router_online15:
    print("CRITICAL: Router is offline")

if cpu_usage15 > 80:
    print("WARNING: High CPU usage")

if not ssh_enabled15:
    print("SECURITY ALERT: SSH is disabled")




router_online16 = True
ssh_enabled16 = True

if router_online16:
    print("Router is online")

    if ssh_enabled16:
        print("SSH is enabled")
    else:
        print("WARNING: SSH is disabled")

else:
    print("CRITICAL: Router is offline")