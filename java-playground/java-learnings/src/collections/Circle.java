package collections;

public class Circle implements Comparable<Circle> {

    int  radius;

    Circle(int radius){
        this.radius=radius;
    }

    public int getRadius() {
        return radius;
    }



    public void setRadius(int radius) {
        this.radius = radius;
    }

    @Override
    public String toString() {
        return "Circle{" +
                "radius=" + radius +
                '}';
    }

    @Override
    public int compareTo(Circle other) {
        return this.radius- other.radius;
//        0 --equals
//        +ve -- my value is higher than other one
//        -ve -- my value is lower that the other one

//        Circle - 10 my circle
//        Circle -20 other circle

    }
}
