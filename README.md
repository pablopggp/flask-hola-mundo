# Flask Hola Mundo

API mínima en Flask desplegada en Vercel como función serverless de Python.

## Estructura

Todo el código vive en `api/index.py`, la función serverless que Vercel despliega. No hay otros archivos de aplicación.

## Endpoint

`GET /` devuelve:

```json
{"mensaje": "Hola mundo"}
```

Desplegado en: https://flask-hola-mundo-pi.vercel.app/

## Ejecutar en local

```bash
pip install -r requirements.txt
flask --app api/index.py run
```

## Despliegue

Cada push a `main` dispara un redeploy automático en Vercel.
