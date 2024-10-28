from netmiko import ConnectHandler

R2 = ConnectHandler (
    device_type='cisco_ios',
    ip='192.168.112.159',
    username='cisco',
    password='123',
    secret='123'
)

R3 = ConnectHandler (
    device_type='cisco_ios',
    ip='192.168.112.160',
    username='cisco',
    password='123',
    secret='123'
)

routers = [R2, R3]

for router in routers:
    router.enable()
    commands = []
    for i in range(1, 4):
        commands.append(f"interface loopback {i}")
        commands.append(f"ip address {i}.{i}.{i}.{i} 255.255.255.0")
        commands.append(f"description LOOPBACK{i}")
    output = router.send_config_set(commands)
    outputResult = router.send_command("show ip int br")
    print("show ip int br: \n{}\n".format(outputResult))
    print("show ip int br: \n{}\n".format(output))