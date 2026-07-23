package collections;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ListDemo {

//    List is an ordered ,duplicate allowing sequence
//    ArrayList --> fast index access | inserting/removing the elements from middle shifts
//    LinkedList --> fast add/remove at ends | slower index access

    public static void main(String[] args) {

        List<String> arrayList=new ArrayList<>();
        List<String> linkedList=new LinkedList<>();

        arrayList.add("iPhone");
        arrayList.add("Galaxy");
        arrayList.add("Pixel");


        linkedList.add("iPhone");
        linkedList.add("Galaxy");
        linkedList.add("Pixel");

        System.out.println(arrayList);
        System.out.println(linkedList);

        for(String name:arrayList){
            System.out.println(name);
        }
        System.out.println("----------------------------------------");
        for(String name:linkedList){
            System.out.println(name);
        }

        Circle c1=new Circle(10);
        Circle c2=new Circle(20);
        Circle c3=new Circle(30);
        Circle c4=new Circle(40);
        Circle c5=new Circle(50);

        List<Circle> listOfCircle=new ArrayList<>();
        listOfCircle.add(c1);
        listOfCircle.add(c2);
        listOfCircle.add(c3);
        listOfCircle.add(c4);
        listOfCircle.add(c5);

        System.out.println(listOfCircle);

    }
}
