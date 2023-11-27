using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab3_NguyenNhatTruong_Bai3_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // tạo Server Endpoint dùng để tham chiếu đến địa chỉ IP và Port của Server
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 5000);

            // tạo Server Socket dùng để kết nối với Server Endpoint
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            Console.WriteLine("Dang ket noi voi server...");
            // lắng nghe kết nối Server Socket
            serverSocket.Connect(serverEndpoint);

            //Xuất thông tin nếu kết nối 
            if (serverSocket.Connected)
            {
                Console.WriteLine("Ket noi thanh cong voi server...");
                byte[] buff = new byte[100];
                int byteReceive = serverSocket.Receive(buff, 0, buff.Length, SocketFlags.None);
                string str = Encoding.ASCII.GetString(buff, 0, byteReceive);
                Console.WriteLine(str);
            }

            Console.ReadKey();
            serverSocket.Close();
        }
    }
}
