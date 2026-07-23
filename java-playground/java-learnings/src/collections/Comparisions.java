package collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Comparisions {

    public static void main(String[] args) {
        List<String> arrayList=new ArrayList<>();


        arrayList.add("iPhone");
        arrayList.add("Galaxy");
        arrayList.add("Pixel");

        System.out.println(arrayList);
        Collections.sort(arrayList);
        System.out.println("After Sort:"+arrayList);


        Circle c1=new Circle(10);
        Circle c2=new Circle(20);
        Circle c3=new Circle(30);
        Circle c4=new Circle(40);
        Circle c5=new Circle(50);

        List<Circle> listOfCircle=new ArrayList<>();

        listOfCircle.add(c2);
        listOfCircle.add(c4);
        listOfCircle.add(c5);
        listOfCircle.add(c1);
        listOfCircle.add(c3);

        System.out.println(listOfCircle);

        Collections.sort(listOfCircle);
        System.out.println("After Sort:"+listOfCircle);

        Collections.sort(listOfCircle,Collections.reverseOrder());
        System.out.println("reverse sort:"+listOfCircle);

    }
}
