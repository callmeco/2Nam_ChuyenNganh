using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
namespace Bai2
{
    internal class Program
    {
        
        static void Main(string[] args)
        {
            Employee emp1 = new Employee();

            TcpClient client;
            try
            {
                client = new TcpClient("127.0.0.1", 9050);
            }
            catch (SocketException)
            {
                Console.WriteLine("Khong ket noi duoc voi server"); return;
            }
            NetworkStream ns = client.GetStream();
            while (true)
            {
                Console.Write("Ma nhan vien: ");
                emp1.EmployeeID = int.Parse(Console.ReadLine());
                Console.Write("Ho nhan vien: ");
                emp1.LastName = Console.ReadLine();
                Console.Write("Ten nhan vien: ");
                emp1.FirstName = Console.ReadLine();
                Console.Write("So nam lam viec: ");
                emp1.YearsService = int.Parse(Console.ReadLine());
                Console.Write("Luong nhan vien: : ");
                emp1.Salary = int.Parse(Console.ReadLine());

                byte[] data = emp1.GetBytes();
                int size = emp1.size;
                byte[] packsize = new byte[2];
                Console.WriteLine("Kich thuoc goi tin = {0}", size);
                packsize = BitConverter.GetBytes(size);
                ns.Write(packsize, 0, 2);
                ns.Write(data, 0, size);
                ns.Flush();
                Console.WriteLine("Ban muon tiep tuc khong: ");
                if(Console.ReadLine() == "Khong")
                    break;

            }

            ns.Close(); 
            client.Close();

        }
        
    }
}
