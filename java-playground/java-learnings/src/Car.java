public class Car {

    String color;
    String name;

    Car(){
        System.out.println("Default Constructor of Car");

    }

    Car(String color){
        this.color=color;

    }

    Car(String color,String name){
        this.color=color;
        this.name=name;
    }

    public void printDetails(){
        System.out.println("Car: color:"+color+" name:"+name);
    }

    public void setColor(String color){
        this.color=color;
    }

    public String getColor(){
        return color;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
