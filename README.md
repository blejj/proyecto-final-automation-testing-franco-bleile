# Proyecto Final - Framework de Automatización de Pruebas

## Propósito del proyecto

Este proyecto consiste en un framework de automatización de pruebas desarrollado en Python, utilizando Selenium WebDriver para pruebas de UI y Requests para pruebas de API.

El objetivo es aplicar buenas prácticas de testing automatizado, como el uso de Page Object Model, parametrización de datos, generación de reportes HTML, manejo de screenshots y estructura modular del framework.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- pytest-html
- WebDriver Manager
- Git & GitHub

## Estructura del proyecto

pages/ → Page Object Model (UI)
tests/ui/ → Tests de interfaz gráfica
tests/api/ → Tests de API
utils/ → Utilidades (logger, screenshots, api client)
data/ → Datos de prueba (JSON)
reports/ → Reportes HTML generados
screenshots/ → Capturas de errores en fallos
logs/ → Logs de ejecución

## Instalación de dependencias

Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

Instalar dependencias:

pip install -r requirements.txt

Cómo ejecutar las pruebas

Ejecutar todos los tests:
pytest

Ejecutar tests con reporte HTML:
pytest --html=reports/report.html --self-contained-html

Cómo interpretar los reportes:
Luego de ejecutar los tests, se genera un reporte HTML en:

reports/report.html

En este reporte podemos ver:

Tests ejecutados
Estado de cada test (PASSED / FAILED)
Tiempo de ejecución
Errores detallados en caso de fallos

Evidencia de fallos (Screenshots):

Si algún test falla, se genera automáticamente una captura en:

screenshots/

Cada imagen incluye el nombre del test y la fecha/hora de ejecución.

Logs de ejecución:

Durante la ejecución se generan logs en:

logs/

Estos logs permiten depurar y analizar la ejecución de los tests.
