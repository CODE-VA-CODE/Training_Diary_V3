import sqlite3


def changeUserTable():
    connection = sqlite3.connect("Trainings.db3")
    query = """
SELECT id as 'ID',
       name as 'Имя',
       age as 'Возраст' 
FROM users
    """
    return connection.cursor().execute(query).fetchall()

def traingsHistoryTable(name):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
            SELECT trainings.date AS Дата,
       trainings.calories AS Калории,
       exercises.exercise AS Тренировка FROM Trainings INNER JOIN exercises
 WHERE trainings.user_id = (
                               SELECT id
                                 FROM users
                                WHERE name = '{name}'
                           ) AND exercises.id=trainings.exercise_id;
"""
    return connection.cursor().execute(query).fetchall()

def userChanged(id):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
SELECT name,
       age,
       height,
       weight FROM users
WHERE users.id = {id}
    """
    return connection.cursor().execute(query).fetchall()

def setNewUser(name, weight, height, age):
    connection = sqlite3.connect("Trainings.db3")
    try:
        query = f"""
    INSERT INTO users(name, age, weight, height) VALUES('{name}', {age}, {height}, {weight})
        """
        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
    except:
        pass

def delUser(name):
    connection = sqlite3.connect("Trainings.db3")
    query_training = f"""
    DELETE from trainings
WHERE trainings.user_id =(SELECT id from users where name = '{name}')
        """
    query_user = f"""
       DELETE from users
WHERE users.id =(SELECT id from users where name = '{name}')
            """
    cur = connection.cursor()
    cur.execute(query_training)
    cur.execute(query_user)
    connection.commit()

def tableDataEdit(oldName, newName, age):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
    UPDATE users
SET name = '{newName}',
    age = {int(age)}
WHERE users.name = '{oldName}'
        """
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def setNewTraining(dateTime, user, trainingType, exers, exSet):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
    INSERT INTO trainings(date, calories, exercise_id, user_id) VALUES('{dateTime}',
      ((SELECT calories FROM exercises WHERE exercise='{trainingType}')*({int(exers)}*{int(exSet)})), 
      (SELECT id FROM exercises WHERE exercise='{trainingType}'),
      (SELECT id FROM users WHERE name='{user}'))
        """
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def setNewWeight(dateTime, weight, user):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
    INSERT INTO weights(date, weight, user_id) VALUES('{dateTime}',
      '{weight}',
      (SELECT id FROM users WHERE name='{user}'))
        """
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

def weightHistoryTable(name):
    connection = sqlite3.connect("Trainings.db3")
    query = f"""
    SELECT weights.date AS Дата,
       weights.weight AS Вес FROM weights
 WHERE weights.user_id = (
                               SELECT id
                                 FROM users
                                WHERE name = '{name}'
                           );
"""
    return connection.cursor().execute(query).fetchall()
