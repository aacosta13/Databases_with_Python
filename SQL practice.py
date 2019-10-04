# Practice real life problems with SQL

import sqlite3


class Car:
    def __init__(self, m=None, v=None):
        self._make = m
        self._vim = v

    def __repr__(self):
        return self._make + ' ' + self._vim + ' '


class School:
    def __init__(self, name=None, sid=None):
        self._name = name
        self._sid = sid
        self._persons = list()

    def add_person(self, person_obj):
        self._persons.append(person_obj)

    def create(sid=None, n=None):
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        sql_stmt = 'INSERT INTO School VALUES ("{0}", "{1}")'.format(sid, n)
        cur.execute(sql_stmt)
        conn.commit()
        conn.close()

    def search(cond=None):
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        if cond is None:
            sql_stmt = 'SELECT * FROM School'
        else:
            sql_stmt = 'SELECT * FROM School WHERE ' + cond
        cur.execute(sql_stmt)
        r_list = cur.fetchall()
        s_list = list()
        for r in r_list:
            school_obj = School(r[0], r[1])
            s_list.append(school_obj)
        return s_list


class Person:
    def __init__(self, fn=None, ln=None, ssn=None):
        self._firstName = fn
        self._lastName = ln
        self._ssn = ssn
        self._cars = list()
        self._schools = list()

    def __repr__(self):
        out_str = 'Name: ' + self._firstName + ' ' + self._lastName + ' '
        for c in self._cars:
            out_str += 'Car: ' + str(c)

        return out_str

    def create(fn=None, ln=None, ssn=None):
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        sql_stmt = 'INSERT INTO Person VALUES ("{0}", "{1}", {2})'.format(fn, ln, ssn)
        cur.execute(sql_stmt)
        conn.commit()
        conn.close()

    def search(cond=None):
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        if cond is None:
            sql_stmt = 'SELECT * FROM Person'
        else:
            sql_stmt = 'SELECT * FROM Person WHERE ' + cond
        cur.execute(sql_stmt)
        r_list = cur.fetchall()
        p_list = list()
        for r in r_list:
            person_obj = Person(r[0], r[1], r[2])
            p_list.append(person_obj)
        for p in p_list:
            p.retrieve_cars()
        return p_list

    def add_car(self, car_obj):
        self._cars.append(car_obj)
        # INSERT A RECORD INTO CAR TABLE
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        sql_stmt = 'INSERT INTO Car VALUES ("{0}", "{1}", {2})'.format(car_obj._make, car_obj._vim, self._ssn)
        cur.execute(sql_stmt)
        conn.commit()
        conn.close()

    def retrieve_cars(self):
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        sql_stmt = 'SELECT * FROM Car WHERE ssn=' + str(self._ssn)
        cur.execute(sql_stmt)
        records = cur.fetchall()
        for Cars in records:
            car = Car(Cars[0], Cars[1])
            self._cars.append(car)
    '''
    def add_school(self, school_obj):
        self._schools.append(school_obj)
        school_obj.add_person(self)
        conn = sqlite3.connect('Test_db_04-11.db')
        cur = conn.cursor()
        sql_stmt = 'INSERT INTO Attendance VALUES ("{0}", "{1}"'.format(self._ssn, school_obj._sid)
        cur.execute(sql_stmt)
        conn.commit()
        conn.close()
    '''

# Below section creates data into DB
'''
Person.create('John', 'Chen', 1234567)
Person.create('Amy', 'Sampson', 1234567)
Person.create('Steve', 'Liu', 1234567)
Person.create('James', 'Chang', 1234567)
'''

# Below creates Person data into DB

person_list = Person.search('lastName="Chen"')
print(person_list)

sList = School.search('name="CSUF"')

pObj = person_list[0]
sObj = sList[0]
#pObj.add_school(sObj)


person_obj = person_list[0]
car_obj = Car('Ford', 'X78789889')
person_obj.add_car(car_obj)

person_obj.retrieve_cars()