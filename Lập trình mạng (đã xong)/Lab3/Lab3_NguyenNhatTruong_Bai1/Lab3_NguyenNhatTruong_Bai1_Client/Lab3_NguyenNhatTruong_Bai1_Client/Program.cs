using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace Lab3_NguyenNhatTruong_Bai1_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 5000);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

            string str = "\nhello server";
            byte[] data = Encoding.UTF8.GetBytes(str);

            Console.WriteLine("Dang gui loi chao len Server");
            serverSocket.SendTo(data, data.Length, SocketFlags.None, serverEndpoint);
            Console.WriteLine("Da gui loi chao len Server");

            Console.ReadKey();
            Console.ReadLine();
        }
    }
}
