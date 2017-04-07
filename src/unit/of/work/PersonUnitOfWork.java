package unit.of.work;


import db.DB;
import domain.Person;
import identity.map.PersonIdentityMap;

import java.util.HashMap;
import java.util.Map;


public class PersonUnitOfWork {

    private Map<Integer, Person> newPersons = new HashMap();
    private Map<Integer, Person> delPersons = new HashMap();

    public void addNewPerson(Integer key, Person p) {
        this.newPersons.put(key, p);
    }

    public void delPerson(Integer key, Person p) {
        this.delPersons.put(key, p);
    }

    public void commit() {
        newPersons.forEach((k, v) -> DB.addPerson(k, v));
    }

}
