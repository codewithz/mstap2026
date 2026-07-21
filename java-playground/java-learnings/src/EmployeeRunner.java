public class EmployeeRunner {

    public static void main(String[] args) {

        Employee emma,thomas;

        thomas=new Employee();
        thomas.printDetails();
        thomas.setName("Thomas G");
        thomas.setAge(30);
        thomas.setSalary(100000D);
        thomas.setManager(false);
        thomas.printDetails();

        System.out.println("--------------------------------------------");

        emma=new Employee("Emma J",30,100000D,true);
        emma.printDetails();

    }
}
