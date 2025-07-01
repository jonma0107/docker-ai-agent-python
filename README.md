# AI Email & Research Assistant

Este proyecto es una aplicación que combina FastAPI, Streamlit y agentes de IA para realizar investigaciones y enviar resultados por correo electrónico. Utiliza LangGraph y LangChain para la gestión de agentes de IA, y PostgreSQL para almacenar el historial de mensajes.

## 🌟 Características

- Interfaz web intuitiva con Streamlit
- API REST con FastAPI
- Agentes de IA para investigación y gestión de correos
- Envío automático de resultados por correo
- Almacenamiento de historial en PostgreSQL
- Dockerizado para fácil despliegue

## 🔗 URLs de Producción

- **Frontend (Streamlit)**: [https://ai-email-research-assistant.streamlit.app/](https://ai-email-research-assistant.streamlit.app/)
- **Backend (FastAPI)**: [https://docker-ai-agent-python-production-0067.up.railway.app/](https://docker-ai-agent-python-production-0067.up.railway.app/)

## 🏗 Estructura del Proyecto

### Backend (FastAPI)

#### Módulos de IA
- `agents.py`: Define los agentes de IA (email_agent y research_agent) y el supervisor
- `assistants.py`: Implementa el asistente de correo electrónico
- `llms.py`: Configuración del modelo de lenguaje OpenAI
- `schemas.py`: Esquemas Pydantic para validación de datos
- `services.py`: Servicios para generar contenido de correos
- `tools.py`: Herramientas que utilizan los agentes (research_email, send_me_email, get_unread_emails)

#### Base de Datos
- `db.py`: Configuración de PostgreSQL con SQLModel
- `models.py`: Modelos de datos para mensajes de chat

#### API
- `routing.py`: Endpoints de la API (/api/chat/)
- `main.py`: Punto de entrada de FastAPI

#### Gestión de Correos
- `gmail_imap_parser.py`: Parser robusto para Gmail vía IMAP
- `inbox_reader.py`: Lectura de correos no leídos
- `sender.py`: Envío de correos vía SMTP

### Frontend (Streamlit)
- `streamlit.py`: Interfaz de usuario web
- `streamlit.Dockerfile`: Configuración de Docker para Streamlit

## 🚀 Configuración y Despliegue

### Requisitos Previos
- Docker y Docker Compose
- Cuenta de Gmail
- API Key de OpenAI

### Variables de Entorno (.env)
```
EMAIL_ADDRESS=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_aplicacion
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
OPENAI_API_KEY=tu_api_key_de_openai
DATABASE_URL=postgresql://usuario:contraseña@db_service:5432/nombre_db
```

### Configuración de Contraseña de Aplicaciones en Gmail

1. **Accede a tu cuenta de Google**:
   - Ve a "Gestionar tu cuenta de Google"
   - Sección "Seguridad"

2. **Habilita la Verificación en dos pasos** (si no está habilitada):
   - Necesario para crear contraseñas de aplicaciones

3. **Crear Contraseña de Aplicación**:
   - Ve a "Contraseñas de aplicaciones"
   - Selecciona "Otra" en el menú desplegable
   - Nombra la aplicación (ej: "AI Agent Test")
   - Copia la contraseña generada de 16 caracteres
   - Usa esta contraseña en la variable EMAIL_PASSWORD

### Despliegue

#### Backend (Railway)
1. **Clonar el repositorio**:
```bash
git clone <repositorio>
cd <repositorio>
```

2. **Configurar variables de entorno en Railway**
3. **Desplegar usando el Procfile existente**:
```
web: uvicorn main:fastapi_app --host 0.0.0.0 --port $PORT
```

#### Frontend (Streamlit Cloud)
1. Ir a [Streamlit Cloud](https://streamlit.io/cloud)
2. Conectar con el repositorio de GitHub
3. Configurar el despliegue:
   - **Main file path**: `backend/src/streamlit.py`
   - **Branch**: main
4. Configurar las variables de entorno necesarias en Streamlit Cloud
5. La app estará disponible en: [https://ai-email-research-assistant.streamlit.app/](https://ai-email-research-assistant.streamlit.app/)

### Desarrollo Local

1. **Configurar variables de entorno**:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

2. **Iniciar con Docker Compose**:
```bash
docker-compose up --build
```

3. **Acceder a la aplicación localmente**:
- Frontend (Streamlit): http://localhost:8501
- Backend (FastAPI): http://localhost:8000

## 📝 Uso

1. **Accede a la interfaz Streamlit** (https://ai-email-research-assistant.streamlit.app/)
2. **Escribe tu consulta** en el campo de texto
3. **Activa la opción de correo** si deseas recibir resultados por email
4. **Ingresa el correo destinatario** si es diferente al predeterminado
5. **Presiona "Enviar"** y espera la respuesta

### Ejemplos de Consultas
```
Research what is the best type of food in different parts of the world and email me the results
```

## 🔧 Mantenimiento

### Logs y Monitoreo
```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend
docker-compose logs -f streamlit
```

### Reiniciar Servicios
```bash
docker-compose restart backend
docker-compose restart streamlit
```

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. 