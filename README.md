# Rest-api

Api creada con Python usando el framework Flask en un solo archivo. 

Contiene 4 rutas: 
    -/productos
    -/descuentos
    -/productos/categorias/<orden>
    -/productos/<name>
  
  La ruta /productos muestra todos los productos con su respectivo nombre, precio y categoria.
  La ruta /descuentos muestra todos los productos que tienen descuento junto con su nombre, precio y categoria.
  La ruta /productos/categorias/<orden> muestra un conjunto de productos de la categoria que se escriba en lugar de <orden>
  La ruta /productos/<name> muestra todos los productos que coincidan con las palabras colocadas en el lugar de <name>
  
  Al colocar una ruta que no se halla definido mandara un mensaje de error con un status 404.
  
  Use solo un archivo ya que no tenia demasiadas rutas, si las rutas hubieran sido mas hubiera usado blueprints. 
