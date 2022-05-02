import java.util.Scanner;

import java.util.Scanner;

public class module9 {

   public static void main(String args[]) {

       Scanner in = new Scanner(System.in);

       int arr[] = new int[20];

       System.out.println("Enter 20 numbers:");

       for (int i = 0; i < 20; i++) {

           arr[i] = in.nextInt();

       }
       }


    double average = total / arr.length;
      
   }

       int Highest = arr[0], Highest = arr[0], sum = 0;

       for (int i = 0; i < arr.length; i++) {

           if (arr[i] < Lowest)

               Lowest= arr[i];

               

           if (arr[i] > Highest)

               Highest= arr[i];

               

           sum += arr[i];

       }

       

       System.out.println("Highest value= " + Highest);

       System.out.println("lowest value = " + Lowest);

       System.out.println("Sum = " + sum);

 System.out.println("The average is: %.3f", average);

   }

public class JAAMinMaxSumAverage

{

   public static void main(String args[]) {

       Scanner in = new Scanner(System.in);

       int arr[] = new int[20];

       System.out.println("Enter 20 numbers:");

       for (int i = 0; i < 20; i++) {

           arr[i] = in.nextInt();

       }

       int min = arr[0], max = arr[0], sum = 0;

       for (int i = 0; i < arr.length; i++) {

           if (arr[i] <Lowest)

               Lowest= arr[i];

               

           if (arr[i] > max)

               max = arr[i];

               

           sum += arr[i];

       }

       

       System.out.println("Highest value = " + Lowest);

       System.out.println("Lowest value = " + Lowest );

       System.out.println("Sum = " + sum);

 System.out.println("The average is: %.3f", average);

   }

}
