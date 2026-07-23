package generics;

//public class Box {
//
//    private  Object item;
//
//    public void put(Object item){
//        this.item=item;
//    }
//
//    public Object get(){
//        return item;
//    }
//}


class Box<T>{
    private T item;
   // private  Object item;
    public void put(T item){
        this.item=item;
    }
    public T get(){
        return  item;
    }
}
