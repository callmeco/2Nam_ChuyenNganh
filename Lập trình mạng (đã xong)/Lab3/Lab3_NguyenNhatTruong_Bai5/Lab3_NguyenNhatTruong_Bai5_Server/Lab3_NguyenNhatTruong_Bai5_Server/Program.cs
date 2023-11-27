using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab3_NguyenNhatTruong_Bai5_Server
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

            for  (int i = 1; i <= 5; i++)
            {
                int byteReceive = serverSocket.ReceiveFrom(buffer, 0, buffer.Length, SocketFlags.None, ref clientEndpoint);
                string str = Encoding.ASCII.GetString(buffer, 0, byteReceive);
                Console.WriteLine(str);
            }
        }
    }
}
