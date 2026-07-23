package deferred;

public class AppleIPhone extends Mobile implements CE,ISO{
    @Override
    public void makeCall() {
        System.out.println("Make Call of Apple IPhone");
    }

    @Override
    public void sendSMS() {
        System.out.println("Send SMS of Apple IPhone");
    }

    public void faceTime(){
        System.out.println("Facetime with Apple");
    }

    @Override
    public void processA() {
        System.out.println("CE:Iphone- Process A");
    }

    @Override
    public void processB() {
        System.out.println("CE:Iphone- Process B");
    }

    @Override
    public void processX() {
        System.out.println("ISO:Iphone- Process X");
    }

    @Override
    public void processY() {
        System.out.println("ISO:Iphone- Process Y");
    }
}
