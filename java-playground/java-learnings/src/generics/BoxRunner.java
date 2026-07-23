package generics;

public class BoxRunner {

    public static void main(String[] args) {
//        Box box=new Box();
//
//        box.put("Not an Integer!");
//
////        Integer integer=(Integer)box.get();
//        String string=(String)box.get();

        Box<Integer> box1=new Box<>();
        box1.put(10);
//        box1.put("10");
        Integer n= box1.get();
        System.out.println("Box :"+n);

        Box<String> box2=new Box<>();
        box2.put("Neueda");
        String s=box2.get();
        System.out.println("Box:"+s);


    }
}
