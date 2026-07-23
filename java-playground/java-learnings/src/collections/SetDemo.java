package collections;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetDemo {

    // No Duplicates

//    HashSet -- Ordering is not guaranteed | Fastest
//    LinkedHashSet -- Ordering in which it was inserted | nearly fast as HashSet
    //TreeSet -- sorted(natural ordering) | slowest of all 3

    public static void main(String[] args) {
        Set<String> hashSet=new HashSet<>();
        Set<String> linkedHashSet=new LinkedHashSet<>();
        Set<String> treeSet=new TreeSet<>();


        String[] brands={"Pixel","iPhone","Galaxy","Pixel"};

        for(String brand:brands){
            hashSet.add(brand);
            linkedHashSet.add(brand);
            treeSet.add(brand);
        }

        System.out.println("HashSet:"+hashSet);
        System.out.println("LinkedHashSet:"+linkedHashSet);
        System.out.println("TreeSet:"+treeSet);
    }
}
