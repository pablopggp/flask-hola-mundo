# Flask Hola Mundo

API mínima en Flask desplegada en Vercel como función serverless de Python.

## Endpoint

`GET /api` devuelve:

```json
{"mensaje": "Hola mundo"}
```

## Ejecutar en local

```bash
pip install -r requirements.txt
flask --app app run
```

La función de Vercel está en `api/index.py`.
