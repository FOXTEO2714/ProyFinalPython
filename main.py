import pymysql
import datetime

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Foxteo2714',
            db='tareaspython'
        )

        self.cursor = self.connection.cursor()

        print("Conexión establecida existosamente")

    def select_tareas(self,id):
        sql = 'SELECT id,descripcion,fecha,usuario,estado FROM TAREAS WHERE id = {}'.format(id) 

        try:
            self.cursor.execute(sql)
            tareas = self.cursor.fetchone()
            if tareas != None:
                print("id:",tareas[0])
                print("descripcion:",tareas[1])
                print("fecha:",tareas[2])
                print("usuario:",tareas[3])
                print("estado:",tareas[4])

            return tareas

        except Exception as e:
            raise e            

    def select_all_tareas(self):
        sql = 'SELECT id,descripcion,fecha,usuario,estado FROM TAREAS' 

        try:
            self.cursor.execute(sql)
            tareas = self.cursor.fetchall()

            for tarea in tareas:
                print("id:",tarea[0])
                print("descripcion:",tarea[1])
                print("fecha:",tarea[2])
                print("usuario:",tarea[3])
                print("estado:",tarea[4])

            return tareas
        except Exception as e:
            raise e             

    def update_tareas(self,id,descripcion,fecha,usuario,estado):
        sql = "UPDATE TAREAS SET descripcion='{}',fecha=TIMESTAMP('{}'),usuario='{}',estado='{}' WHERE id={}".format(descripcion,fecha,usuario,estado,id) 

        try:
            self.cursor.execute(sql)   
            self.connection.commit()
            tarea = self.select_tareas(id)
            json = {
                "message": "Tarea actualizada correctamente",
                "tarea" : tarea
            }
            return json            
        except Exception as e:
            json = {
                "message": "La Tarea no fue actualizada correctamente",
                "error" : "{}".format(e)
            }
            return json
    
    def delete_tareas(self, id):
        TareaBuscada = self.select_tareas(id)
        message = ""
        if TareaBuscada == None:
            message = "Tarea no encontrada"
        else:
            message = "Tarea eliminada correctamente",
        sql = "DELETE FROM TAREAS WHERE id={}".format(id) 

        try:
            self.cursor.execute(sql)   
            self.connection.commit()  
            
            json = {
                "message" : message,
                "Lista de Tareas" : self.select_all_tareas()
            }
            return json
        except Exception as e:
            print(str(e))
            json = {
                "message" : "Tarea no eliminada" ,
                "error" : "{}".format(e)
            }
            return json

    def insert_tareas(self, descripcion,fecha,usuario,estado):
        sql = "INSERT INTO TAREAS (descripcion, fecha, usuario, estado) VALUES('{}', current_timestamp ,'{}','{}')".format(descripcion,usuario,estado) 
        print(sql)
        try:    
            self.cursor.execute(sql)   
            self.connection.commit()  
            json = {
                "message" : "Registro Insertado",
                "tareas" : self.select_all_tareas()
            }
            return json
                                 
        except Exception as e:
            print(str(e))
            return "Registro no Insertado"    

    def close(self):
        self.connection.close()        

    

database = DataBase()

#intente ingresar mi fecha de cumpleaños 1967, pero por el tipo de datos timestamp, no pude realizarlo, ya que permite fechas de 1970-2038
database.update_tareas(8,"Tarea9","1980-10-01","Diego Maradona","Actualizda")
database.select_all_tareas()

database.close()

