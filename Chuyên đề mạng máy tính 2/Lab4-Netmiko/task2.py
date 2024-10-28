from netmiko import ConnectHandler

R2 = ConnectHandler (
    device_type='cisco_ios',
    ip='192.168.112.159',
    username='cisco',
    password='123',
    secret='123'
)

R4 = ConnectHandler (
    device_type='cisco_ios',
    ip='192.168.112.161',
    username='cisco',
    password='123',
    secret='123'
)

routers = [R2, R4]

def save_config_file(router, filename):
    router.enable()
    output = router.send_command("show run")
    with open (filename, 'w') as file:
        file.write(output)
    
    print(f"Cau hinh show run duoc luu vao file: {filename}")

def load_config_file(router, filename):
    router.enable()
    with open(filename, 'r') as file:
        commands = file.readlines()
    
    output = router.send_config_set(commands)
    print(f"Tu file {filename} da duoc cau hinh")
    print(output)

save_config_file(R2, 'fileCauhinhR2.txt')
load_config_file(R4, "fileCauhinhR2.txt")