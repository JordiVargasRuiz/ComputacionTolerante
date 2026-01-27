# Secure Login Simulator

Un simulador seguro de sistema de inicio de sesión desarrollado en Python con interfaz gráfica. Implementa validación de credenciales, manejo de errores personalizado y logging de eventos de seguridad.

## Características

✅ **Interfaz gráfica intuitiva** - Desarrollada con Tkinter  
✅ **Validación de credenciales** - Usuario y contraseña requeridos  
✅ **Manejo de errores personalizado** - Excepciones específicas para cada caso  
✅ **Bloqueo de cuenta** - Después de 3 intentos fallidos  
✅ **Logging de seguridad** - Registra errores en archivo `security.log`  
✅ **Diseño moderno** - Interfaz con tema oscuro y colores cibernéticos  

## Estructura del Proyecto

```
login_secure_python/
├── main.py           # Interfaz gráfica principal
├── auth.py           # Lógica de autenticación
├── errors.py         # Excepciones personalizadas
├── logger.py         # Sistema de logging
└── security.log      # Registro de errores (generado al ejecutar)
```

## Módulos

### `main.py`
Interfaz gráfica con Tkinter que contiene:
- Campos de entrada para usuario y contraseña
- Botón de inicio de sesión
- Manejo de mensajes de éxito y error

### `auth.py`
Funcionalidad de autenticación:
- Validación de campos vacíos
- Verificación de longitud mínima de contraseña (4 caracteres)
- Validación de credenciales
- Control de intentos fallidos
- Bloqueo automático después de 3 intentos

### `errors.py`
Jerarquía de excepciones personalizadas:
- `LoginError` - Clase base
- `EmptyFieldError` - Campos vacíos
- `InvalidCredentialsError` - Usuario/contraseña incorrectos
- `AccountLockedError` - Cuenta bloqueada por intentos excesivos

### `logger.py`
Sistema de logging que:
- Registra errores en `security.log`
- Incluye marca de tiempo y nivel de severidad
- Captura eventos de seguridad

## Requisitos

- Python 3.6+
- Tkinter (incluido en la mayoría de instalaciones de Python)

## Instalación

1. Clona o descarga el proyecto:
```bash
git clone <repository-url>
cd login_secure_python
```

2. No hay dependencias externas que instalar

## Uso

Ejecuta el programa:

```bash
python main.py
```

### Credenciales de prueba
- **Usuario:** `admin`
- **Contraseña:** `1234`

### Flujo de uso
1. Ingresa el usuario y contraseña
2. Haz clic en "INICIAR SESIÓN"
3. El sistema validará las credenciales
4. Si son correctas, recibirás un mensaje de bienvenida
5. Si hay errores, recibirás mensajes de error específicos

## Reglas de validación

- ❌ No se permiten campos vacíos
- ❌ La contraseña debe tener mínimo 4 caracteres
- ❌ Las credenciales deben coincidir exactamente
- 🔒 Cuenta bloqueada después de 3 intentos fallidos

## Logging

Todos los errores se registran automáticamente en el archivo `security.log` con:
- Marca de tiempo
- Nivel de severidad
- Mensaje de error

## Ejemplo de log
```
2026-01-27 10:15:23,456 - ERROR - Campos vacíos
2026-01-27 10:15:45,789 - ERROR - Credenciales incorrectas
2026-01-27 10:16:12,345 - ERROR - Credenciales incorrectas
```

## Mejoras futuras

- Base de datos para usuarios reales
- Hashing de contraseñas
- Autenticación de dos factores
- Interfaz web
- API REST

## Autor

Desarrollado como parte del proyecto de Computación Tolerante a Fallos

## Licencia

MIT
