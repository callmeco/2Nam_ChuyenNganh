using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab3_NguyenNhatTruong_Bai5_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 0);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

            serverSocket.Connect(serverEndpoint);

            for (int i = 1; i <= 5; i++)
            {
                byte[] buff = Encoding.ASCII.GetBytes("thong diep "+ i.ToString());
                serverSocket.SendTo(buff, 0, buff.Length, SocketFlags.None, serverEndpoint);
            }

            Console.WriteLine("Da thoat chuong trinh");
            Console.ReadLine();
            serverSocket.Close();
        }
    }
}
