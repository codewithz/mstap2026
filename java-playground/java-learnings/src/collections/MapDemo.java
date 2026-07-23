package collections;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class MapDemo {

//    Map --Key , Value Pair
//    Same ordering story as Set

//    HashMap
//    LinkedHashMap
//    TreeMap -- sorted by Key

    public static void main(String[] args) {

        Map<String,Integer> hashMap=new HashMap<>();
        Map<String,Integer> linkedHashMap=new LinkedHashMap<>();
        Map<String,Integer> treeMap=new TreeMap<>();

        String[] brands={"Pixel","iPhone","Galaxy"};
        int[] years={2016,2007,2009};

        for(int index=0;index<brands.length;index++){
            hashMap.put(brands[index],years[index]);
            linkedHashMap.put(brands[index],years[index]);
            treeMap.put(brands[index],years[index]);

        }


        System.out.println("Hash Map:"+hashMap);
        System.out.println("Linked Hash Map:"+linkedHashMap);
        System.out.println("Tree Map:"+treeMap);
    }
}
