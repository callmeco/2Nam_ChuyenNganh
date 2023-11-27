using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab3_NguyenNhatTruong_Bai4_Server
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Any, 5000);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

            serverSocket.Bind(serverEndpoint);
            Console.WriteLine("Dang cho Client ket noi toi...");

            EndPoint clientEndpoint = new IPEndPoint(IPAddress.Any, 0);

            byte[] buffer = new byte[1024];
            int receivedByte;

            while (true)
            {
                buffer = new byte[1024];
                receivedByte = serverSocket.ReceiveFrom(buffer, ref clientEndpoint);
                string str = Encoding.UTF8.GetString(buffer, 0, receivedByte);
                Console.WriteLine(clientEndpoint + str);
            }
        }
    }
}
