public class MethodsRunner {

    public static void main(String[] args) {

        MethodsDemo md=new MethodsDemo();

        md.sayHello();
        md.add(10,15);
        int taxRate=md.getTaxRate();
        System.out.println("Tax Rate:"+taxRate);
        int square=md.getSqaureValue(12);
        System.out.println("Square is:"+square);

    }
}
