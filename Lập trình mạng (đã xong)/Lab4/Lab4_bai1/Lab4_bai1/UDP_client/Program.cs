using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
namespace UDP_client
{
    internal class Program
    {
        static void Main(string[] args)
        {

            EndPoint serverEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 5600);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram,
ProtocolType.Udp);
            // Vut bo het tat ca cac goi tin UDP khong den tu serverEndPoint
            serverSocket.Connect(serverEndPoint);
            byte[] buff;
            //string str = "Hello Server";
            //buff = Encoding.ASCII.GetBytes(str);
            //serverSocket.SendTo(buff, buff.Length, SocketFlags.None, serverEndPoint);
            //serverSocket.ReceiveFrom(buff, ref serverEndPoint);
            int i = 10;
            while (true)
            {
                RetryUdpClient();
                //string input = Console.ReadLine();
                //if (input == "exit")
                    //break;
            }
        }
        private static int SndRcvData(UdpClient s, byte[] message, IPEndPoint rmtdevice)
        {
            IPEndPoint sender = new IPEndPoint(IPAddress.Any, 0);
            EndPoint Remote = (EndPoint)(sender);
            int recv;
            int retry = 0;
            byte[] data;
            while (true)
            {
                Console.WriteLine("Truyen lai lan thu: #{0}", retry);
                try
                { 
                    s.Send(message, message.Length);
                    data = s.Receive(ref rmtdevice);
                    return data.Length;
                }
                catch (SocketException)
                {
                    return 0;
                }
            }
        }
        public static void RetryUdpClient()
        {
            byte[] data;
            string input, stringData;
            int recv;
            UdpClient server = new UdpClient();
            IPEndPoint ipep = new IPEndPoint(IPAddress.Any, 0);
            server.Connect("127.0.0.1", 5600);
            string welcome = "Hello Server";
            data = Encoding.ASCII.GetBytes(welcome);
            recv = SndRcvData(server, data, ipep);
            if (recv > 0)
            {
                stringData = Encoding.ASCII.GetString(data, 0, recv);
                Console.WriteLine(stringData);
            }
            else
            {
                Console.WriteLine("Khong the lien lac voi thiet bi o xa");
                return;
            }
            while (true)
            {
                input = Console.ReadLine();
                if (input == "exit")
                    break;
                recv = SndRcvData(server, Encoding.ASCII.GetBytes(input), ipep);
                if (recv == 0)
                    Console.WriteLine("Khong nhan duoc cau tra loi");
            }
            Console.WriteLine("Dang dong client");
            server.Close();
        }
    }
}
