using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace Lab2_NguyenNhatTruong_Bai2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // tạo Server Endpoint dùng để tham chiếu đến địa chỉ IP và Port của Server
            IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Any, 5000);

            // tạo Server Socket dùng để kết nối với Server Endpoint
            Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            // lắng nghe kết nối Server Socket
            serverSocket.Bind(serverEndpoint);
            serverSocket.Listen(10);
            Socket clientSocket = serverSocket.Accept();

            //Xuất thông tin nếu kết nối 
            EndPoint clientEndpoint = clientSocket.RemoteEndPoint;
            Console.WriteLine(clientEndpoint.ToString());

            byte[] buff;
            string hello = "Hello Client";
            buff = Encoding.ASCII.GetBytes(hello);
            clientSocket.Send(buff, 0, buff.Length, SocketFlags.None);

            Console.ReadKey();
        }
    }
}
