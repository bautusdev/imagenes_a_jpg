import os
from PIL import Image

# Directorio de entrada y salida (usa la ruta actual si están ahí mismo)
carpeta_origen = "./imagenes"
carpeta_destino = "./jpg"

# Crear la carpeta de salida si no existe
os.makedirs(carpeta_destino, exist_ok=True)

# Extensiones de imagen válidas a buscar
formatos_validos = (".png", ".webp", ".bmp", ".tiff", ".gif", ".jpeg",".avif",".tif")

# Recorrer todos los archivos en la carpeta de origen
for archivo in os.listdir(carpeta_origen):
  if archivo.lower().endswith(formatos_validos):
    ruta_origen = os.path.join(carpeta_origen, archivo)

    try:
      # Abrir la imagen
      with Image.open(ruta_origen) as img:
        # Convertir a RGB (necesario si la imagen original tiene transparencia PNG/WEBP)
        img_rgb = img.convert("RGB")

        # Cambiar la extensión del archivo a .jpg
        nombre_base = os.path.splitext(archivo)[0]
        ruta_destino = os.path.join(carpeta_destino, f"{nombre_base}.jpg")

        # Guardar en formato JPG con calidad de 100%
        img_rgb.save(ruta_destino, "JPEG", quality=100)
        print(f"Convertido: {archivo} -> {nombre_base}.jpg")

    except Exception as e:
      print(f"No se pudo convertir {archivo}: {e}")
