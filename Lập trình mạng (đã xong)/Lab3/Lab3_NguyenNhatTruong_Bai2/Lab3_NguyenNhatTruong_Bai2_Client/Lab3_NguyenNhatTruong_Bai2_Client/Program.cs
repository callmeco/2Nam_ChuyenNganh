using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab3_NguyenNhatTruong_Bai2_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 5000);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

            string str = Console.ReadLine();
            if (str.Equals("exit"))
            {
                serverSocket.Close();
                Console.WriteLine("Thoat chuong trinh Client");
                Console.ReadLine();
                return;
            }

            byte[] data = Encoding.UTF8.GetBytes(str);

            Console.WriteLine("Dang gui loi chao len Server");
            serverSocket.SendTo(data, data.Length, SocketFlags.None, serverEndpoint);
            Console.WriteLine("Da gui loi chao len Server");

            Console.ReadKey();
            Console.ReadLine();
        }
    }
}
