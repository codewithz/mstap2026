package exceptions;

public class ExceptionDemo {

    public static void main(String[] args) {

        try {
            int[] storageSizes={128,256,512};
            System.out.println(storageSizes[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
        finally {
            System.out.println("This runs no matter what");
        }

        System.out.println("Program runs normally...");

        try {
            int result = 10 / 10;
            String brand="Apple";
            System.out.println(brand.length());
            String storageText="128GB";
            int storage=Integer.parseInt(storageText);
        }
        catch (ArithmeticException e){
            System.out.println("Arithemetic Exception");
            System.out.println(e.getMessage());
        }
        catch (Exception e) {
            System.out.println("Generic Exception:"+e);
            System.out.println(e.getMessage());
        }

    }
}
