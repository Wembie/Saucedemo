# Proyecto de Pruebas Unitarias para Saucedemo

Este repositorio contiene un conjunto de pruebas unitarias para la aplicación Saucedemo. El proyecto está organizado en distintas categorías de pruebas y utiliza un entorno virtual (venv) para gestionar las dependencias.


## Requisitos Previos

- **Python 3.x**: Asegúrate de tener Python instalado.
- **Virtualenv**: Utiliza un entorno virtual para manejar las dependencias.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Wembie/Saucedemo.git
   ```

2. Accede al directorio del proyecto:
    ```bash
    cd Saucedemo/Pruebas\ Unitarias
    ```

3. Activa el entorno virtual:
    ```bash
    source venv/bin/activate   # En Linux o macOS
    .\venv\Scripts\activate    # En Windows
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de Pruebas
Para ejecutar todas las pruebas unitarias, utiliza el siguiente comando:

```bash
python -m unittest discover tests
```

También puedes ejecutar un archivo de prueba específico, como test_cart.py:

```bash
python -m unittest tests/test_cart.py
```

## Capturas de Pantalla
Las capturas de pantalla de los resultados de las pruebas se encuentran en la carpeta screenshots/, organizadas por tipo de prueba.