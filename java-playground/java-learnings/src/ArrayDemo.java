public class ArrayDemo {

    public static void main(String[] args) {

//     1. Declare
//     2. Construct
//     3. Initialize

        int[] numbers;

        numbers = new int[5];
        System.out.println("Just after constructing");
        printArray(numbers);

        numbers[0] = 35;
        numbers[1] = 23;
        numbers[2] = 43;
        numbers[3] = 98;
        numbers[4] = 23;
//        numbers[5]=35;

        System.out.println("After Initializing");
        printArray(numbers);

        Pen[] penArrays;
        penArrays=new Pen[3];
        Pen p1,p2,p3;
        p1=new Pen();
        p2=new Pen();
        p3=new Pen();

        penArrays[0]=p1;
        penArrays[1]=p2;
        penArrays[2]=p3;

        for(Pen p:penArrays){
            p.openCap();
            p.write();
            p.closeCap();
        }


    }

        public static void printArray(int[] array){
            int arrayLength=array.length;

            for(int index=0;index<arrayLength;index++){
                int value=array[index];
                System.out.println("Index "+index+" : "+value);
            }
        }
    }

