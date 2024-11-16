use std::collections::HashSet;
use std::io;

struct SistemaUsuarios {
    usuarios_permitidos: HashSet<String>,
}

impl SistemaUsuarios {
    fn new() -> Self {
        let mut usuarios = HashSet::new();
        usuarios.insert("Jhonatan".to_string());
        usuarios.insert("Miguel".to_string());
        usuarios.insert("Paula".to_string());
        usuarios.insert("Edgar".to_string());

        SistemaUsuarios {
            usuarios_permitidos: usuarios,
        }
    }

    fn iniciar_sesion(&self, usuario: &str) {
        if self.usuarios_permitidos.contains(usuario) {
            println!("Bienvenido, has iniciado sesión como: {}", usuario);
        } else {
            println!("Acceso denegado para: {}", usuario);
        }
    }

    fn agregar_usuario(&mut self, admin: &str, nuevo_usuario: &str) {
        if self.usuarios_permitidos.contains(admin) {
            if self.usuarios_permitidos.insert(nuevo_usuario.to_string()) {
                println!("Usuario '{}' agregado correctamente por {}.", nuevo_usuario, admin);
            } else {
                println!("El usuario '{}' ya existe.", nuevo_usuario);
            }
        } else {
            println!("{} no tiene permiso para agregar usuarios.", admin);
        }
    }

    fn eliminar_usuario(&mut self, admin: &str, usuario_a_eliminar: &str) {
        if self.usuarios_permitidos.contains(admin) {
            if self.usuarios_permitidos.remove(usuario_a_eliminar) {
                println!("Usuario '{}' eliminado correctamente por {}.", usuario_a_eliminar, admin);
            } else {
                println!("El usuario '{}' no existe.", usuario_a_eliminar);
            }
        } else {
            println!("{} no tiene permiso para eliminar usuarios.", admin);
        }
    }

    fn listar_usuarios(&self) {
        println!("Usuarios permitidos: {:?}", self.usuarios_permitidos);
    }
}

fn main() {
    let mut sistema = SistemaUsuarios::new();

    
    sistema.iniciar_sesion("Paula"); 
    sistema.iniciar_sesion("Carlos");  

   
    sistema.agregar_usuario("Paula", "Carlos");  
    sistema.agregar_usuario("Carlos", "Luna");   

    
    sistema.listar_usuarios();  

    // Eliminar un usuario
    sistema.eliminar_usuario("Paula", "Carlos");  
    sistema.eliminar_usuario("Carlos", "Luna");   

    
    sistema.listar_usuarios();  
}