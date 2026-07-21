public class Employee {

    String name;
    int age;
    double salary;
    boolean isManager;

    Employee(){

    }

    Employee(String name,int age,double salary,boolean isManager){
        this.name=name;
        this.age=age;
        this.salary=salary;
        this.isManager=isManager;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public boolean isManager() {
        return isManager;
    }

    public void setManager(boolean manager) {
        isManager = manager;
    }

    public void printDetails(){
        System.out.println("Name:"+name);
        System.out.println("Age:"+age);
        System.out.println("Salary:"+salary);
        System.out.println("Is Manager:"+isManager);
    }
}
