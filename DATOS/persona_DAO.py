from DOMINIO.persona import Persona


class PersonaDAO:
    _INSERT = ("INSERT INTO Personas (nombres, apellidos, cedula, sexo, email)"
               "VALUES (?, ?, ?, ?, null)")

   # @classmethod
    #def insertar_persona(cls, persona):
       # with Conexion.obtenerCursor() as cursor:
           # datos = (persona.nombre, persona.apellido, persona.cedula, persona.sexo,)
           # cursor.execute(cls._INSERT, datos)


if __name__ == '_main_':
    p1 = Persona(cedula="0954556688", nombre="Marco", apellido="Castillo", sexo="Masculino")
   # PersonaDAO().insertar_persona(p1)