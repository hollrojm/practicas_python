import logging

logger = logging.getLogger(__name__) # Se crea un logger personalizado

logger.setLevel(logging.DEBUG) # Se define el nivel del logger


handler_consola = logging.StreamHandler() # Se crea un manejador de consola
formato_logs = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S") # Se define el formato de los logs

handler_consola.setFormatter(formato_logs) # Se le asigna el formato al manejador de consola

logger.addHandler(handler_consola) # Se añade el manejador de consola al logger     

logger.info("Este es un mensaje de info") # Se envía un mensaje de info
logger.error("Este es un mensaje de errorrrrrrr") # Se envía un mensaje de error

handler_archivo = logging.FileHandler("app.log") # Se crea un manejador de archivo
handler_archivo.setLevel(logging.ERROR) # Se define el nivel del manejador de archivo
handler_archivo.setFormatter(formato_logs) # Se le asigna el formato al manejador de archivo
logger.addHandler(handler_archivo) # Se añade el manejador de archivo al logger