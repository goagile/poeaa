package identity.map;


import domain.Person;

import java.util.HashMap;
import java.util.Map;


public class PersonIdentityMap {
    private Map<Integer, Person> persons = new HashMap<>();

    public static void main(String... args) {
        PersonIdentityMap map = new PersonIdentityMap();
        map.addPerson(123, new Person("Ilia"));
        for(Person p : map.persons.values()) {
            System.out.println(p.name);
        }
    }

    public void addPerson(Integer key, Person p) {
        this.persons.put(key, p);
    }
}
