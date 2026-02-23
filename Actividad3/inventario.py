import json
import os

# ==========================================
# 1. CLASE PRODUCTO
# ==========================================
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    # Método para convertir el objeto a un diccionario (útil para el JSON)
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    # Método de clase para crear un Producto desde un diccionario (útil para leer el JSON)
    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["precio"], data["cantidad"])

    # Método para mostrar el producto de forma legible
    def __str__(self):
        return f"📦 {self.nombre.capitalize()} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}"


# ==========================================
# 2. CLASE INVENTARIO
# ==========================================
class Inventario:
    def __init__(self):
        # Usamos un diccionario donde la clave es el nombre (en minúsculas) para búsquedas rápidas
        self.productos = {}

    # --- 3. FUNCIONES PRINCIPALES ---

    def agregar_producto(self, producto):
        nombre_key = producto.nombre.lower()
        if nombre_key in self.productos:
            # Si el producto ya existe, le sumamos la cantidad
            self.productos[nombre_key].cantidad += producto.cantidad
            print(f"✅ Se actualizó la cantidad de '{producto.nombre}'. Nueva cantidad: {self.productos[nombre_key].cantidad}")
        else:
            self.productos[nombre_key] = producto
            print(f"✅ Producto '{producto.nombre}' agregado al inventario.")

    def eliminar_producto(self, nombre):
        nombre_key = nombre.lower()
        if nombre_key in self.productos:
            del self.productos[nombre_key]
            print(f"🗑️ Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"⚠️ Error: El producto '{nombre}' no existe en el inventario.")

    def buscar_producto(self, nombre):
        nombre_key = nombre.lower()
        if nombre_key in self.productos:
            return self.productos[nombre_key]
        return None

    def listar_productos(self):
        print("\n--- LISTA DE PRODUCTOS ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
        print("--------------------------\n")

    # --- 4. CALCULAR VALOR TOTAL ---
    def calcular_valor_total(self):
        total = sum(p.precio * p.cantidad for p in self.productos.values())
        return total

    # --- 5. GUARDAR Y CARGAR EN JSON ---
    def guardar_en_json(self, nombre_archivo):
        # Convertimos cada objeto Producto a diccionario
        datos = [producto.to_dict() for producto in self.productos.values()]
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"💾 Inventario guardado con éxito en '{nombre_archivo}'.")

    def cargar_desde_json(self, nombre_archivo):
        if not os.path.exists(nombre_archivo):
            print(f"⚠️ El archivo '{nombre_archivo}' no existe. Se iniciará un inventario vacío.")
            return

        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            self.productos.clear() # Limpiamos el inventario actual
            for item in datos:
                nuevo_producto = Producto.from_dict(item)
                self.productos[nuevo_producto.nombre.lower()] = nuevo_producto
        print(f"📂 Inventario cargado con éxito desde '{nombre_archivo}'.")


# ==========================================
# EJEMPLO DE USO
# ==========================================
if __name__ == "__main__":
    archivo_bd = "inventario_tienda.json"
    mi_tienda = Inventario()

    # Si hay un archivo anterior, lo carga
    mi_tienda.cargar_desde_json(archivo_bd)

    # 1. Agregar productos
    print("\n--- AGREGANDO PRODUCTOS ---")
    p1 = Producto("Teclado Mecanico", 45.50, 10)
    p2 = Producto("Raton Inalambrico", 25.00, 15)
    p3 = Producto("Monitor 24 pulgadas", 120.00, 5)
    
    mi_tienda.agregar_producto(p1)
    mi_tienda.agregar_producto(p2)
    mi_tienda.agregar_producto(p3)

    # Comprobación de que suma cantidades si el producto ya existe
    p_repetido = Producto("Teclado Mecanico", 45.50, 5)
    mi_tienda.agregar_producto(p_repetido)

    # 2. Listar productos
    mi_tienda.listar_productos()

    # 3. Buscar producto
    print("--- BUSCANDO PRODUCTO ---")
    busqueda = mi_tienda.buscar_producto("raton INALAMBRICO")
    if busqueda:
        print(f"Encontrado: {busqueda}")
    else:
        print("Producto no encontrado.")

    # 4. Eliminar producto
    print("\n--- ELIMINANDO PRODUCTO ---")
    mi_tienda.eliminar_producto("Monitor 24 pulgadas")

    # 5. Valor total del inventario
    print("\n--- VALOR TOTAL ---")
    valor = mi_tienda.calcular_valor_total()
    print(f"💰 El valor total del inventario actual es: ${valor:.2f}")

    # 6. Guardar en JSON (Si ejecutas este código, verás que se crea un archivo de texto en tu carpeta)
    print("\n--- GUARDANDO BASE DE DATOS ---")
    mi_tienda.guardar_en_json(archivo_bd)