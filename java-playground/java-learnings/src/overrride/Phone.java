package overrride;

import java.util.Objects;

public class Phone {

    private String name;
    private int memory;

    public Phone() {
    }

    public Phone(String name, int memory) {
        this.name = name;
        this.memory = memory;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }

    @Override
    public boolean equals(Object obj) {
        if(obj == null){
            return false;
        }
        if(obj instanceof Phone){
            Phone other=(Phone) obj;
            return name.equals(other.getName()) && memory == other.getMemory();
        }
        return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name,memory);
    }

    @Override
    public String toString() {
        return name+"  "+memory+ "GB";
    }
}
