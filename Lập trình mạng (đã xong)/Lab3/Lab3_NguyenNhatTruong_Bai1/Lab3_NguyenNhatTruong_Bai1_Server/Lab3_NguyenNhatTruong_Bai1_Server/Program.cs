using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace Lab3_NguyenNhatTruong_Bai1_Server
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 5000);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            serverSocket.Bind(serverEndpoint);
            Console.WriteLine("Dang cho client ket noi toi...");
            EndPoint clientEndpoint = new IPEndPoint(IPAddress.Any, 0);

            byte[] buffer = new byte[1024];

            int receivedByte;

            receivedByte = serverSocket.ReceiveFrom(buffer, ref clientEndpoint);
            string str = Encoding.UTF8.GetString(buffer, 0, receivedByte);

            Console.WriteLine("Da ket noi toi Server " + str);

            Console.ReadKey();
            Console.ReadLine();
            serverSocket.Close();
        }
    }
}
