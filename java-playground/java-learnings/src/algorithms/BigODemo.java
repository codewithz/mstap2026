package algorithms;

public class BigODemo {

    static int sink=0; // accumulating real work

    public static void main(String[] args) {
        int[] sizes={5000,10000,20000,40000,80000};

        System.out.println("n\tO(n) time (ms)\t O(n^2) time (ms)");

        for(int n:sizes){
            long linearTime=timeLinear(n);
            long quadraticTime=timeQuadratic(n);
            System.out.println("For Size :"+n+" | Linear Time:"+linearTime+" | Quadratic Time:"+quadraticTime);
        }
        System.out.println("sink="+sink+" Ignore this-- it just stops the JVM cheating");


    }

//    O(n): one pass over n times

    static long timeLinear(int n){
        long start=System.nanoTime();

        for(int i=0;i<n;i++){
            sink+=i;
        }
        long end=System.nanoTime();
        long milliseconds=(end-start)/1000000;
        return  milliseconds;
    }

//    O(n^2) : every item is compared against every other item
    static long timeQuadratic(int n){
        long start=System.nanoTime();

       for(int i=0;i<n;i++){
           for (int j=0;j<n;j++){
               sink+=1;
           }
       }
        long end=System.nanoTime();
        long milliseconds=(end-start)/1000000;
        return  milliseconds;
    }
}
