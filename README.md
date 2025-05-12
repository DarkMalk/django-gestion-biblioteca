# Library System

Este proyecto es una plataforma diseñada para gestionar libros y préstamos de manera eficiente. Construida con Django como framework backend y TailwindCSS para el diseño frontend, ofrece una solución moderna y escalable para bibliotecas y sistemas de gestión de recursos bibliográficos.

## Requisitos

- **Python**: v3.12 (recomendada)

# Lista de tareas en Notion

Puedes revisar las tareas pendientes o ya completadas en el siguiente enlace: [Ir a notion](https://www.notion.so/1f1e90013c10800996d5d77ebbd19be7?v=1f1e90013c10813bb25d000c41febc53&pvs=4).

## Cómo empezar

### MacOS/Linux

1. Genera un entorno virtual:

```bash
python3.12 -m venv .venv
```

2. Activa el entorno virtual:

```bash
source .venv/bin/activate
```

### Windows

1. Genera un entorno virtual:

```bash
python -m venv .venv
```

2. Activa el entorno virtual:

```bash
.venv\Scripts\Activate.bat
```

## Instalación de dependencias

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Aplica las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Modo desarrollo

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

## Crear super usuario para panel administrativo de Django

```bash
python manage.py createsuperuser
```
