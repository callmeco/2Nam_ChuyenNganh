using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace Lab3_NguyenNhatTruong_Bai3_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 0);
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

            while (true)
            {
                string str = Console.ReadLine();
                
                if (str.Equals("exit"))
                {
                    break;
                }
                byte[] buff = Encoding.UTF8.GetBytes(str);
                serverSocket.SendTo(buff, 0, buff.Length, SocketFlags.None, serverEndpoint);
                Console.WriteLine("Da gui thong tin");

                Console.ReadKey();
                Console.WriteLine();
            }

            Console.WriteLine("Da thoat chuong trinh");
            Console.ReadLine();
            serverSocket.Close();
        }
    }
}
