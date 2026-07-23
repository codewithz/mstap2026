package overrride;

public class PhoneRunner {

    public static void main(String[] args) {
        Phone p1=new Phone("iPhone",128);
        Phone p2=new Phone("iPhone",128);

//        System.out.println(p1.getClass().getSuperclass());
        System.out.println(p1.equals(p2));

        System.out.println(p1.hashCode());
        System.out.println(p2.hashCode());

        System.out.println(p1);
        System.out.println(p2);
    }
}
