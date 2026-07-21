public class CarRunner {

    public static void main(String[] args) {

        Car car1,car2,car3;

        car1=new Car();
        car1.printDetails();
        car1.setColor("Black");
        car1.setName("Honda City");
        car1.printDetails();

        System.out.println("-------------------------------------------------------------------");
        car2=new Car("White");
        car2.printDetails();
        car2.setName("Hyundai Venue");
        car2.printDetails();
        System.out.println("-------------------------------------------------------------------");
        car3=new Car("White","Camry");
        car3.printDetails();

    }
}
