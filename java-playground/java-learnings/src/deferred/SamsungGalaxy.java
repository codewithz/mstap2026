package deferred;

public class SamsungGalaxy extends Mobile{
    @Override
    public void makeCall() {
        System.out.println("Make Call of Galaxy");
    }

    @Override
    public void sendSMS() {
        System.out.println("Send SMS of Galaxy");
    }

    public void galaxyAI(){
        System.out.println("Galaxy Ai");
    }
}
