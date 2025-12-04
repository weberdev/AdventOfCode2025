// See https://aka.ms/new-console-template for more information
using System;
long total = 0;
string day2Input = "78847-119454,636-933,7143759788-7143793713,9960235-10043487,44480-68595,23468-43311,89-123,785189-1014654,3829443354-3829647366,647009-692765,2-20,30-42,120909-197026,5477469-5677783,9191900808-9191943802,1045643-1169377,46347154-46441299,2349460-2379599,719196-779497,483556-641804,265244-450847,210541-230207,195-275,75702340-75883143,58-84,2152-3237,3367-5895,1552-2029,9575-13844,6048-8966,419388311-419470147,936-1409,9292901468-9292987321";
List<string> choppedInput = new List<string>();
choppedInput = day2Input.Split(',').ToList();
List<long[]> SKUsets= new List<long[]>();
foreach(string SKUSet in choppedInput)
{
    string[] SKUstrings = SKUSet.Split("-");
    long[] SKUrange = new long[2];
    SKUrange[0]=long.Parse(SKUstrings[0]);
    SKUrange[1]=long.Parse(SKUstrings[1]);
    SKUsets.Add(SKUrange);
}
foreach (long[] SKUpair in SKUsets)
{
    /*foreach(long SKU in SKUpair)
    {
        Console.WriteLine(SKU);
    }
    Console.WriteLine("next");
    */
    for (long i = SKUpair[0]; i < SKUpair[1]; i++)
    {
        long digits = (long)Math.Floor(Math.Log10(i)) + 1;
        if (digits % 2 == 0)
        {
            long half = digits / 2;
            long tenfold = (long)Math.Pow(10,(long)half);
            long valHolder = i / tenfold;
            if (i-valHolder == valHolder * tenfold)
            {
                Console.WriteLine(i);
                total += i;
            }
        }
    }
}
Console.WriteLine(total);