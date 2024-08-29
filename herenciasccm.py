'''
Tenemos 'Personas' que se a su vez se dividen en 3 tipos: Futbolista, Entrenador, Masajista.
Lo que tienen todos en común es: id, nombre, apellidos, edad.
Para futbolista se agrega: dorsal, demarcacion.
Para entrenador se agrega: id_federacion
Para masajista se agrega: titulacion, annosexperiencia

Entre las acciones que realizan se encuentran:
Todos: concentrar, viajar.
Furbolista:jugar, entrenar.
Entrenador: dirigir partido, dirigir entrenamiento
Masajista: masajear

'''

# Defino la clase principal
class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def concentrar(self):
        return f"{self.nombre} {self.apellidos} está concentrado durante un mes completo."
    
    def viajar(self):
        return f"{self.nombre} {self.apellidos} está viajando a su destino."


# Defino la herencia1: Futbolista  
class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    def jugar(self):
        return f"{self.nombre} {self.apellidos} está jugando como {self.demarcacion} con el dorsal {self.dorsal}."
    
    def entrenar(self):
        return f"{self.nombre} está entrenando."


# Defino la herencia2: Entrenador  
class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion

    def dirigir_partido(self):
        return f"{self.nombre} está dirigiendo el partido de fútbol."

    def dirigir_entrenamiento(self):
        return f"{self.nombre} está dirigiendo el entrenamiento con el equipo."


# Defino la herencia3: Masajista  
class Masajista(Persona):  
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosexperiencia):
        super().__init__(id, nombre, apellidos, edad) 
        self.titulacion = titulacion
        self.annosexperiencia = annosexperiencia
    
    def masajear(self):
        return f"{self.nombre} {self.apellidos} está realizando un masaje. Tiene {self.annosexperiencia} años de experiencia en su área."


# Futbolistas
marcelo_salas = Futbolista("12909990-8", "Marcelo", "Salas", 31, 11, "delantero/a")
fernanda_pinilla = Futbolista("210112976-1", "Fernanda", "Pinilla Roa", 30, 17, "defensor/a")
claudio_bravo = Futbolista("14599167-3", "Claudio", "Bravo Muñoz", 41, 13, "portero/a")
yanara_aedo = Futbolista("18599167-3", "Yanara", "Aedo Muñoz", 31, 10, "delantero/a")

# Entrenadores
ricardo_gareca = Entrenador("22246543-6", "Ricardo", "Gareca Nardi", 66, 98778)
luis_mena = Entrenador("22346533-6", "Luis", "Mena Irarrázabal", 45, 98775) #Selección de fútbol femenino chileno

# Masajistas
alejandro_orizola = Masajista("26065941-1", "Alejandro", "Orizola Molina", 58, "Traumatólogo y Ortopedista", 28)
mauricio_huerta = Masajista("13895802-1", "Mauricio", "Huerta García", 39, "Masoterapeuta", 12)

print("\nEJEMPLOS DE USO: ")
print("================\n")

print(marcelo_salas.jugar(), "\n")

print(f"{marcelo_salas.nombre} {marcelo_salas.apellidos} fue un gran {marcelo_salas.demarcacion} en la selección chilena. \n")

print(f"El número de {marcelo_salas.nombre} {marcelo_salas.apellidos} es {marcelo_salas.id}.\n")

print(marcelo_salas.concentrar(), "\n")

print(fernanda_pinilla.viajar(), "\n")

print(claudio_bravo.jugar(), "\n")

print(yanara_aedo.entrenar(), "\n")

print(ricardo_gareca.dirigir_partido(), "\n")

print(luis_mena.dirigir_entrenamiento(), "\n")

print(alejandro_orizola.masajear(), "\n")

print(mauricio_huerta.masajear(), "\n")

print(f"{marcelo_salas.nombre} juega como {marcelo_salas.demarcacion}.\n")

print(f"{fernanda_pinilla.nombre} usa el dorsal número {fernanda_pinilla.dorsal}.\n")

print(f"{alejandro_orizola.nombre} {alejandro_orizola.apellidos} tiene una titulación en {alejandro_orizola.titulacion}.\n")

print(f"{mauricio_huerta.nombre} tiene {mauricio_huerta.annosexperiencia} años de experiencia.\n")

print(f"{luis_mena.nombre} {luis_mena.apellidos} tiene el ID de federación {luis_mena.id_federacion}.\n")

print(ricardo_gareca.viajar(), "\n")

print(alejandro_orizola.concentrar(), "\n")
