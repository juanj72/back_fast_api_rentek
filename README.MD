Traté de implementar un **modelo** **vista**(realmente no tiene parte visual, solo la de Swagger UI que trae por defecto para documentar la API) **controlador**, 

**Comandos inicializadores**

primero instalar las dependencias
y tambien de preferencia yo me acostumbré a usar entornos virtuales

en windows es "py -m venv **[nombre_entorno]**" por defecto acostumbro a ponerle venv segun la docu de python


una vez creado, por favor incluir en el .gitignore, para no cargar el repo en caso de que se quieran hacer algun push o pull request


inciar entorno con: 

windows --> ** \[nombre_entorno]\Scripts\activate **
linux --> source venv/bin/activate

no sé que manejador de paquetes es de preferencia, yo uso pip o pip3, la sentencia sería: **pip install -r requirements.txt

una vez hecho lo anterior, iniciar el server debug con uvicorn (es para levantar el server que por defecto trae segun la docu de FastAPI)

la sentencia para levantar el server sería:  uvicorn [nombre de la clase instanciadora de FastAPI] en mi caso es main, y la variable contenedora app

todo sería:  "uvicorn main:app --reload"

dejé el script de la base de datos para que se pueda correr, y agilizar el proceso de creacion de la misma, tambien deje exportado el paquete de colecciones de la API


