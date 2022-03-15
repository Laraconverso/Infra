##### Notas tomadas durante las clases sincronicas y asincronicas.
---
# <span style="color:lightgreen;">Modulo 1</span>
## <span style="color:violet;">Clase 1</span>
---
### <span style="color:purple"> _Notas del material_</span>
#### Introduccion a la materia 
¿Qué es infraestructura de IT?</br>
La infraestructura de tecnología de la información, o infraestructura de IT, se refiere a los componentes combinados necesarios para el funcionamiento y la gestión de los servicios de IT de la empresa y los entornos de IT.


¿Por qué es tan importante la infraestructura de IT?
La tecnología es el motor de prácticamente todos los aspectos de las empresas actuales. Desde el trabajo de un empleado individual hasta las operaciones de bienes y servicios. Si se conecta correctamente, la tecnología se puede optimizar para mejorar la comunicación, crear eficiencia y aumentar la productividad.

Si una infraestructura de IT es flexible, fiable y segura, puede ayudar a una empresa a cumplir sus objetivos y a ofrecer una ventaja competitiva en el mercado. De forma alternativa, si una infraestructura de IT no se implementa correctamente, las empresas pueden afrontar problemas de conectividad, productividad y seguridad, como infracciones e interrupciones del sistema. En general, contar con una infraestructura correctamente implementada puede ser un factor clave para la rentabilidad de un negocio.

Con una infraestructura de IT, una empresa puede:

- Ofrecer una experiencia del cliente positiva proporcionando acceso ininterrumpido a su sitio web y la tienda en línea.
- Desarrollar y lanzar soluciones al mercado con rapidez.
- Recopilar datos en tiempo real para tomar decisiones rápidas.
- Mejorar la productividad de los empleados.

</br>

### <span style="color:purple;"> _Notas de clase_ </span>
La arquitectura clientr servidor esta compuesta por trees pilares el servidor, middleware y el cliente.

Detallar que hace cada uno
el Middleware es el que se encarga de hacer todo el proceso de por medio entre el click de un cliente y la respuesta del servidor.
Por ejemplo una API, dbms. 

--> Actividad en clase en Jamboard [Link](https://jamboard.google.com/d/1YSi-O1wf46oiqJAOVtJmUOmIvHur9i7LiNlk8Eychks/edit?usp=sharing)

---
# <span style="color:lightgreen;">Modulo 2</span>
## <span style="color:violet;">Clase 2</span>
----
### <span style="color:purple"> _Notas del material_</span>

... </br>

### <span style="color:purple;"> _Notas de clase_ </span>

Automatizar:
Beneficios: 
- Elevar la productividad empresarial.
- Reducir costos operativos.
- Disminuir los riegos de fallas.
- Elevar la seguridad de la informacion.
- Tener una mejor capacidad de respuesta.
- Facilidad de adaptacion.
- Alojar una mayor cantidad de datos.
- Elevar la competitividad del negocio.

Virtualizacion: evaluar la compatibilidad y los distintos entornos. 

Provisioners y Providers

Interfaz de comandos: https://www.vagrantup.com/docs/cli
https://app.vagrantup.com/boxes/search

--> actividad de clase crear la maquina virtual debian con vagrant y tambien de forma manual 
haa

## <span style="color:violet;">Clase 4</span>
----
### <span style="color:purple"> _Notas del material_</span>
Introduccion a la terminal de linux
Comandos utiles:</br>
[LINK ](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)a la cheatsheet de los comandos mas usados.</br>
```mkdir dir1``` genera una carpeta con el nombre dado (en este caso dir1).</br>
```touch dir1/archivo_1.txt``` crea un archivo en el lugar indicado. </br>
```ls -R ``` se listan todos los directorios. </br>
```ls ``` enlista los diferentes archivos de un directorio. </br>
``ls -a `` enlista todo el contenido dentro del directorio incluyendo elementos que se encuentren ocultos.</br>
`ls -l` enlista el contenido e incluye informacion referente a cada elemento.</br>
`rmdir ` elimina un directorio. </br>
`rm ` elimina archivos suueltos. </br>
`rm dir1/archivo_1.txt` aca se elimina el archivo especifico dentor del dir1.</br>
`rm -r dir2` con el modificador -r eliminamos el dir2 y todo su contenido.</br>
`cp ` se pueden copiar archivos y directorios, asi como ubicarlos en otras rutas, definiendo origen primero y luego el destino. </br>
`mv` se usa para mover archivos</br>
`locate ` nos localiza un archivo con el flag `-i` nos busca el archivo independientemente de las mayusculas o minusculas del nombre.</br>
`find` nos permite decirles que ejecute comandos a parte de buscar el archivo o la carpeta. </br>

+++ faltan agregar algunos comandos 
+ La actividad de las mesas se realizo en la maquina virtual. 

## <span style="color:violet;">Clase 5</span>
---
### <span style="color:purple;"> _Notas del material_</span>
Shell srcipting
Bash es una interfaz interprete (que interpreta las ordenes que el usuario le hace al sistema) en la consola de Unix, tambien se pueden realizar a traves de un archivo llamado srcipt. </br>
bash hereda sh, zsh y csh, es la interfaz determinada actualmente en gnu/linux y macos (unix).
</br>
Escribimos en la consola </br>
... </br>
Tipos de variables: </br>
Globales o de entorno</br>
    El sistema Linux establece algunas varibales de entorno globales cuando inciamos sesion en nuestro sstema y siempre son en LETRAS MAYUSCULAS. Si queremos ver las variables de entorno que estamos usando y que estan cargadas en nuestra sesion, escribimos le comando printenv o env en nuestro shell.</br> 
    Para declara una variable global se escribe</br>
    ` export NOMBERVARIABLE=valor ` </br>
    Para acceder a la misma utilizamos la sentencia `$NOMBREVARIABLE` </br>
De usuarios o locales</br>
    Las varibales del tipo usuario o lacl tienen la particularidad que pueden ser accedidas solo por el usuario y la sesion en la que fueron creadas. Una variable local se declara de la forma sencilla:</br>
    `nombrevariable=valor`</br>
    Para acceder a la misma utilizamos la sentencia: `$nombrevariable`.  </br>

 --> VER estructuras de control en bash 
Pruebo en VM. 

### <span style="color:purple;"> _Notas de clase_ </span>
Hacemos dos scripts llamando a dos apis
</br>
 
## <span style="color:violet;">Clase 6</span>
----
### <span style="color:purple"> _Notas del clase_</span>
Hacemos un script llamando a una api similar al de la clase 5.
</br>

## <span style="color:violet;">Clase 7</span>
----
### <span style="color:purple"> _Notas del material_</span>
Intro a Powershell</br>
Comandos `cmdlet` --> retorna una instancia de un objeto.</br>
+ comandos extensibles
+ alias de comandos 
+ se pueden crear nuevos cmdlet
Powersell se utiliza para:
- Automatizar
- Compilar
- Probar
- Implementar
Mas caracterisitcas de poweshell:</br>
- extensible mediante funciones, clases, scripts y modulos.
- Sistema de fomrmato extensible para una salida facil.
- Sistema de tipos extensible para crear tipos dinamicos.
- Compatibilidad integrada con formatos de datos comunes.
--> Poweshell es un proyecto de codigo abierto. </br>
</br>
Los usos mas comunes de powershell son:</br>
+ Automatizacion de tareas: PowerShell sirve para facilitar a los administradores de sistemas las tareas de automatización, administración y configuración de sistemas. 
+ Configuratio management: Al utilizar PowerShell DSC.</br>
+ Monitoreo: Para escribir scripts que pueden ser utilizados por un software de monitoreo. </br>
+ Testear infraestructura: Las pruebas de infraestructura en Pester son código de PowerShell que ejecuta el módulo Pester PowerShell y se crea de una manera específica, conocida como lenguaje específico de dominio (DSL). Este DSL describe el estado deseado y tiene el código necesario para verificar ese estado y comparar el resultado.<br>
+ Automatización de procesos:Automatizar tareas en un proceso de liberación de software (CI/CD).</br>
<br>
Como utilizar un modulo de poweshell???</br>
1er. Instalar el modulo. </br>
2do. Buscar los comandos que agrego el modulo.</br>
3er. Utilizar los comandos que agrego el modulo. </br>
</br>
Como encontrar modulos instalados??
Comandos:

</br>

### <span style="color:purple"> _Notas de clase_</span>
Utilizamos powershell para resolver lo ejercicios pedidos. 
## <span style="color:violet;">Clase 8</span>
----
### <span style="color:purple;"> _Notas del material_</span>
Python:</br>
Jugue con los operadores de python en el archivo dentro de la carpeta `./C8/play.py `
</br>
</br>
</br>
</br>

-----
# <span style="color:lightgreen;">Modulo ..</span>
## <span style="color:violet;">Clase ?</span>
----
### <span style="color:purple;"> _Notas del material_</span>

... </br>

### <span style="color:purple;"> _Notas de clase_ </span>
