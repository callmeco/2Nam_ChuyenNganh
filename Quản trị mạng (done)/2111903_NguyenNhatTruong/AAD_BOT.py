import argparse
import datetime
import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess

ngayGio = datetime.datetime.now()

class MonitorService(rpyc.Service):
    def on_connect(self, connection):
        print('\nĐã kết nối {}'.format(ngayGio))

    def on_disconnect(self, connection):
        print('Đã ngắt kết nối {}\n'.format(ngayGio))

    def exposed_run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as er:
            print(er.returncode)
            print(er.output)

def main():
    prs = argparse.ArgumentParser(description='Automate Active Directory')
    prs.add_argument('-port', type=int, help="Nhập số port")
    args = prs.parse_args()
    port = args.port
    if not port:
        port = 5900
    t = ThreadedServer(MonitorService, port=port)
    t.start()

if __name__ == "__main__":
    main()