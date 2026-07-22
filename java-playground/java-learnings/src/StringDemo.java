public class StringDemo {

    public static void main(String[] args) {

        String s="Operating System";
        System.out.println(s);

        System.out.println("----------- concat ---------");
        String s1=" Management";
        String s2=s.concat(s1);
        System.out.println(s);
        System.out.println(s1);
        System.out.println(s2);

        String s3=s+s1;
        System.out.println(s3);

        System.out.println("----------- length ---------");
        int length=s.length();
        System.out.println(s+" length is "+length);
        int length1=s1.length();
        System.out.println(s1+" length is "+length1);

        System.out.println("----------- equality ---------");

        String x1="Neueda Inc";
        String x2="neueda inc";

        System.out.println(x1.equals(x2)); //checks for exact match including cases
        System.out.println(x1.equalsIgnoreCase(x2));

        System.out.println("----------- Trims and Empty Checks ---------");

        String s4="      Pizza Party    ";
        System.out.println(s4);
        String s5=s4.trim();
        System.out.println(s5);

        String s6="";
        System.out.println("Empty check for s6:"+s6.isEmpty());
        System.out.println("Empty check for s5:"+s5.isEmpty());

        System.out.println("----------- index and char at ---------");

        String s7="Standard";

        char c=s7.charAt(2);
        System.out.println(s7);
        System.out.println(c);
        //     0  1  2  3  4  5  6  7
        //     S  t  a  n  d  a  r  d

        int index1=s7.indexOf("d");
        System.out.println("Index of d is : "+index1);

        int index2=s7.indexOf("d",index1+1);
        System.out.println("Index of d is : "+index2);

        int indexZ=s7.indexOf("z");
        System.out.println("Index of z is : "+indexZ);

        System.out.println("----------------- Upper Case and Lower Case -----");
        System.out.println(x2 + "------------------>"+x2.toUpperCase());
        System.out.println(x1 + "------------------>"+x1.toLowerCase());

        System.out.println("----------------- Replace and Split -----");

        String s8="Jxvx";
        String s9=s8.replaceAll("x","a");
        System.out.println(s8+"----->"+s9);

        String data="1,Tom,IT,Developer,350000";
        String[] dataArray=data.split(",");

        for(String d:dataArray){
            System.out.println(d);
        }

        System.out.println("----------------- Substring -----");

        String s10="Hamburger";
        System.out.println(s10);
        //     0  1  2  3  4  5  6  7  8
        //     H  a  m  b  u  r  g  e  r
        //     1  2  3  4  5  6  7  8  9

        String s11=s10.substring(3);
        System.out.println(s11);

        String s12=s10.substring(4,8);
        System.out.println(s12);

        String value="Internationalization";

//        Inter | nation | national | ion | Intern | ern | liz | on
       //             0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16   17   18 19
      //              I  n  t  e  r  n  a  t  i  o  n    a  l   i   z   a   t    i    o  n




    }
}
