package domain;


public class Person {

    public String name;

    public Person(String name) {
        this.name = name;
    }

    public void print() {
        System.out.println(this.name);
    }

}
