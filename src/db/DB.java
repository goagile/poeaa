package db;

import domain.Person;

import java.util.HashMap;
import java.util.Map;


public class DB {

    private static Map persons = new HashMap();

    public static void addPerson(int key, Person p) {
        persons.put(key, p);
    }

}
