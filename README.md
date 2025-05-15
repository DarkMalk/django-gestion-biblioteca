# Library System

Este proyecto es una plataforma diseñada para gestionar libros y préstamos de manera eficiente. Construida con Django como framework backend y TailwindCSS para el diseño frontend, ofrece una solución moderna y escalable para bibliotecas y sistemas de gestión de recursos bibliográficos.

## Requisitos

- **Python**: v3.12 (recomendada)
- **Node.JS**: v22.11.0 (recomendada)

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

# Para que se usa Node.JS en el proyecto?

En el proyecto se utiliza Node.JS con el propósito de construir con el framework de tailwindcss un archivo css final con **solo** las clases que utilizamos en todo el proyecto, en vez de importar todas las clases disponibles de tailwindcss que no necesitemos.

Para ello tenemos dos comandos que podemos utilizar para realizar la `build` del archivo final de tailwindcss.

Primero debemos instalar las dependencias de tailwind, por lo que debemos utilizar un manejador de paquetes como `npm` o `pnpm`, etc.

```bash
npm install
```

El script `styles:build` nos permitirá realizar una build final una vez por comando.

```bash
node --run styles:build
```

El script `styles:watch` nos permite realizar una build a medida que vayamos desarrollando, por lo que ira revisando los cambios que hagamos en el proyecto para incluirlo en el archivo final ds css.

```bash
node --run styles:watch
```
