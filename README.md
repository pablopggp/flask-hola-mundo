# Flask Hola Mundo

API mínima en Flask con un endpoint `GET /` que devuelve:

```json
{"mensaje": "Hola mundo"}
```

## Ejecutar en local

```bash
pip install -r requirements.txt
flask --app app run
```

## Producción

```bash
gunicorn app:app
```
