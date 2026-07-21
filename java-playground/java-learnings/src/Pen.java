public class Pen {

    int inkLevel=100;

    public void openCap(){
        System.out.println("Open Cap of Pen");
    }

    public void write(){
        inkLevel-=5;
        System.out.println("Ink Level:"+inkLevel);
    }

    public void closeCap(){
        System.out.println("Close Cap of Pen.");
    }
}
