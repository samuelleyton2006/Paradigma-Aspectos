class SistemaUsuarios:
    def __init__(self):
        # Lista de usuarios permitidos
        self.usuarios_permitidos = ["Jhonatan", "Miguel", "Paula", "Edgar"]

    def decorador_seguridad(func):
        def wrapper(self, usuario, *args):
            if usuario in self.usuarios_permitidos:
                return func(self, usuario, *args)
            else:
                print(f"Acceso denegado para: {usuario}")
                return None
        return wrapper

    @decorador_seguridad
    def iniciar_sesion(self, usuario):
        print(f"Bienvenido, has iniciado sesión como: {usuario}")

    @decorador_seguridad
    def agregar_usuario(self, admin, nuevo_usuario):
        # Solo los administradores pueden agregar usuarios
        if admin in self.usuarios_permitidos:
            if nuevo_usuario not in self.usuarios_permitidos:
                self.usuarios_permitidos.append(nuevo_usuario)
                print(f"Usuario '{nuevo_usuario}' agregado correctamente por {admin}.")
            else:
                print(f"El usuario '{nuevo_usuario}' ya existe.")
        else:
            print(f"{admin} no tiene permiso para agregar usuarios.")

    @decorador_seguridad
    def eliminar_usuario(self, admin, usuario_a_eliminar):
        if admin in self.usuarios_permitidos:
            if usuario_a_eliminar in self.usuarios_permitidos:
                self.usuarios_permitidos.remove(usuario_a_eliminar)
                print(f"Usuario '{usuario_a_eliminar}' eliminado correctamente por {admin}.")
            else:
                print(f"El usuario '{usuario_a_eliminar}' no existe.")
        else:
            print(f"{admin} no tiene permiso para eliminar usuarios.")

    @decorador_seguridad
    def listar_usuarios(self, usuario):
        print("Usuarios permitidos:", self.usuarios_permitidos)

# Ejemplos de uso
sistema = SistemaUsuarios()

sistema.iniciar_sesion("Paula")  # Bienvenido, has iniciado sesión como: Paula
sistema.iniciar_sesion("Carlos")  # Acceso denegado para: Carlos

# Agregar nuevos usuarios
sistema.agregar_usuario("Paula", "Carlos")  # Usuario 'Carlos' agregado correctamente por Paula.
sistema.agregar_usuario("Carlos", "Luna")   # Carlos no tiene permiso para agregar usuarios.

# Listar usuarios permitidos
sistema.listar_usuarios("Paula")  # Usuarios permitidos: ['Jhonatan', 'Miguel', 'Paula', 'Edgar', 'Carlos']

# Eliminar un usuario
sistema.eliminar_usuario("Paula", "Carlos")  # Usuario 'Carlos' eliminado correctamente por Paula.
sistema.eliminar_usuario("Carlos", "Luna")   # Carlos no tiene permiso para eliminar usuarios.

# Verificar la lista de usuarios nuevamente
sistema.listar_usuarios("Paula")  # Usuarios permitidos: ['Jhonatan', 'Miguel', 'Paula', 'Edgar']