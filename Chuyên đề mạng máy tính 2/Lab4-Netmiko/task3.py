from netmiko import ConnectHandler

R5 = ConnectHandler (
    device_type='cisco_ios',
    ip='192.168.112.162',
    username='cisco',
    password='123',
    secret='123'
)

R5.enable()

config_commandsLB1 = [
 'interface loopback 1',
 'ip address 2.2.2.2 255.255.255.0',
 'description HIHIHI'
 ]

output = R5.send_config_set(config_commandsLB1)
print("show ip int br: \n{}\n".format(output))


config_commandsLB2 = [
 'interface loopback 2',
 'ip address 3.3.3.3 255.255.255.0',
 'description HAHAHA'
 ]

output = R5.send_config_set(config_commandsLB2)
print("show ip int br: \n{}\n".format(output))

outputResult = R5.send_command("show ip int br")
print("show ip int br: \n{}\n".format(outputResult))

outputCopied = R5.send_command("write memory")
print("write memory: \n{}\n".format(outputCopied))
