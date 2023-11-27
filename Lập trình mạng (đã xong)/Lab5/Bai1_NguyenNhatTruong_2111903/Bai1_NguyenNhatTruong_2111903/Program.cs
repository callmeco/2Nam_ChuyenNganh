using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Bai1_NguyenNhatTruong_2111903
{
    public class MyThreadClass
    {
        private const int Random_Sleep_Max = 1000;
        private const int Loop_Count = 10;

        private string greeting;
        public MyThreadClass(String greeting)
        {
            this.greeting = greeting;
        }

        public void runMyThread()
        {
            Random rand = new Random();
            for (int x = 0; x < Loop_Count; x++)
            {
                Console.WriteLine(greeting + "(Thread ID: " + Thread.CurrentThread.GetHashCode() + ")");
                try
                {
                    Thread.Sleep(rand.Next(0, Random_Sleep_Max));
                }
                catch (ThreadInterruptedException)
                {
                }
            }
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            MyThreadClass mtc1 = new MyThreadClass("Tieu trinh thu nhat");
            Thread thread1 = new Thread(new ThreadStart(mtc1.runMyThread));
            thread1.Start();

            MyThreadClass mtc2 = new MyThreadClass("Tieu trinh thu hai");
            Thread thread2 = new Thread(new ThreadStart(mtc2.runMyThread));
            thread2.Start();

            Console.ReadKey();
        }
    }
}
