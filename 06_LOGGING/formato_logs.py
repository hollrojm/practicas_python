"""Logging.El proceso que conocemos como logging hace referencia al proceso que 
hacemos en desarrollo de software para obtener los logs de nuestros programas.
Un log es un registro que nos ayuda a entender el comportamiento del programa,
ya que al definir un log estamos indicando la ocurrencia de algún evento"""

import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%H:%M:%S")
                    

nombre = "Hollman"
logging.error(f"El usuario {nombre} ha fallado al ingresar la contraseña")
logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje de info")
logging.warning("Este es un mensaje de warning")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje de critical")

try:
    dividir = 10/0
except:
    logging.exception("Ha ocurrido un error al dividir entre cero")