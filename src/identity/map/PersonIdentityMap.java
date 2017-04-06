package identity.map;


import domain.Person;

import java.util.HashMap;
import java.util.Map;


public class PersonIdentityMap {
    private Map<Integer, Person> persons = new HashMap<>();

    public static void main(String... args) {
        PersonIdentityMap map = new PersonIdentityMap();
        map.addPerson(123, new Person("Ilia"));
        Person result = map.getPerson(123);
        result.print();
    }

    public void addPerson(Integer key, Person p) {
        this.persons.put(key, p);
    }

    public Person getPerson(Integer key) {
        return this.persons.get(key);
    }
}
