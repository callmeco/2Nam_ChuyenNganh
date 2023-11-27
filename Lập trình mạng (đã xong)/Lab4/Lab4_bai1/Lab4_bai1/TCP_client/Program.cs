using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
namespace TCP_client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //IPEndPoint serverEndpoint = new IPEndPoint(IPAddress.Loopback, 5600);
            //Socket serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            //Console.WriteLine("Dang ket noi voi server ...");
            //serverSocket.Connect(serverEndpoint);
            TcpClient client = new TcpClient("127.0.0.1", 5600);
            Byte[] data = System.Text.Encoding.ASCII.GetBytes("Hello server!");
            NetworkStream stream = client.GetStream();
            stream.Write(data, 0, data.Length);

            Console.WriteLine("Sent: {0}", "Thong bao");
            data = new Byte[256];
            String responseData = String.Empty;
            Int32 bytes = stream.Read(data, 0, data.Length);
            responseData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
            Console.WriteLine("Received: {0}", responseData);



            //if (serverSocket.Connected)
            //{
            //    byte[] buff = new byte[1024];
            //    buff = new byte[1024];
            //    string str = Console.ReadLine();
            //    Console.WriteLine("Ket noi thanh cong voi server ...");
            //    int byteReceive = serverSocket.Receive(buff, 0, buff.Length, SocketFlags.None);
            //    str = Encoding.ASCII.GetString(buff, 0, byteReceive);
            //    Console.WriteLine(str);
            //}
            //try
            //{
            //    serverSocket.Connect(serverEndpoint);
            //}
            //catch (SocketException ex)
            //{
            //    Console.WriteLine(ex.Message);
            //    return;
            //}
            while (true)
            {
                byte[] buff;
                buff = new byte[1024];
                string str = Console.ReadLine();
                buff = Encoding.ASCII.GetBytes(str);
                // serverSocket.Send(buff, 0, buff.Length, SocketFlags.None);
                stream.Write(buff, 0, buff.Length);
                buff = new byte[1024];
                int byteReceive = stream.Read(buff, 0, buff.Length);
                str = Encoding.ASCII.GetString(buff, 0, byteReceive);
                Console.WriteLine(str);
            }



            Console.ReadKey();
        }
    }
}
