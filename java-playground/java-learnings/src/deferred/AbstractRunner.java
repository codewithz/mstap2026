package deferred;

public class AbstractRunner {
    public static void main(String[] args) {
        Mobile m=new AppleIPhone();
        m.makeCall();
        m.sendSMS();
//        m.faceTime();   --> method slicing happened here

        AppleIPhone iphone=new AppleIPhone();
        iphone.faceTime();
        iphone.makeCall();
        iphone.sendSMS();
        iphone.processA();
        iphone.processB();
        iphone.processX();
        iphone.processY();

        Mobile m1=new SamsungGalaxy();
        m1.makeCall();
        m1.sendSMS();

        System.out.println("Super class for IPhone"+iphone.getClass().getSuperclass());
        System.out.println("Super class for Mobile"+m.getClass().getSuperclass());




    }
}
