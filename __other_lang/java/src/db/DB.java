package db;

import domain.Person;

import java.util.HashMap;
import java.util.Map;


public class DB {

    public static Map<Integer, Person> persons = new HashMap();

    public static void addPerson(Integer key, Person p) {
        persons.put(key, p);
    }

}
