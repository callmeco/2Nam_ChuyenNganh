using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;
using System.IO;
namespace server_tcp_employee
{
    internal class Program
    {
        static void Main(string[] args)
        {
            byte[] data = new byte[1024]; 
            TcpListener server = new TcpListener(IPAddress.Any, 9050);
            server.Start();
            while(true)
            {
                TcpClient client = server.AcceptTcpClient(); 
                NetworkStream ns = client.GetStream();
                try
                {
                    byte[] size = new byte[2];
                    int recv = ns.Read(size, 0, 2);
                    int packsize = BitConverter.ToInt16(size, 0);
                    Console.WriteLine("Kich thuoc goi tin = {0}", packsize);
                    recv = ns.Read(data, 0, packsize);
                    Employee emp1 = new Employee(data);
                    Console.WriteLine("emp1. EmployeeID {0}", emp1.EmployeeID);
                    Console.WriteLine("emp1.LastName = {0}", emp1.LastName);
                    Console.WriteLine("emp1. FirstName = {0}", emp1.FirstName);
                    Console.WriteLine("emp1.Years Service = {0}", emp1.YearsService);
                    Console.WriteLine("emp1.Salary = {0}\n", emp1.Salary);

                    
                    String filepath = "D:\\Đại Học Học Cũng Nhàn ;-;\\Lập trình mạng\\Lab4\\Lab4_bai1\\Lab4_bai1\\ds.txt";
                    FileStream fs = new FileStream(filepath, FileMode.Create);         
                    StreamWriter sWriter = new StreamWriter(fs, Encoding.UTF8);
                    sWriter.WriteLine("");
                    sWriter.Flush();
                    fs.Close();
                }
                catch(SocketException)
                {
                    ns.Close();
                    client.Close();
                }
            }
            


            server.Stop();
        }
}
}
