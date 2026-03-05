# OpenClaw-Sandbox

Sandbox repository for testing OpenClaw coding/testing workflow.

## Greeting API (Python)

The source of truth for the greeting is `hello.py:greet`.
A tiny HTTP API is exposed from `api.py`.

### Run the API

```bash
python3 api.py
```

API endpoint:

- `GET http://127.0.0.1:8000/greeting` → `{ "greeting": "Hello, World!" }`

## Frontend (React + Vite)

A minimal React app is available in `frontend/` and fetches `/greeting` from the Python API.

### Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Then open the local URL printed by Vite (typically `http://127.0.0.1:5173`).

If your API runs on a different host/port, set:

```bash
VITE_API_BASE=http://127.0.0.1:8000 npm run dev
```

## Checks

Run Python tests:

```bash
python3 -m unittest
```

Run frontend build check:

```bash
cd frontend
npm run build
```
