import time
from fastapi import FastAPI, HTTPException, Request
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI(title="capstone-api")
REQS = Counter("http_requests_total", "Requetes HTTP", ["method", "path", "status"])
LAT = Histogram("http_request_duration_seconds", "Latence HTTP", ["path"])


@app.middleware("http")
async def metrics_mw(request: Request, call_next):
    t0 = time.time()
    resp = await call_next(request)
    REQS.labels(request.method, request.url.path, str(resp.status_code)).inc()
    LAT.labels(request.url.path).observe(time.time() - t0)
    return resp


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": True}


@app.get("/predict")
def predict(x: float = 0.0):
    return {"input": x, "label": "positive" if x >= 0 else "negative"}


@app.get("/error")
def error():
    raise HTTPException(status_code=500, detail="erreur simulee (TP 9)")


app.mount("/metrics", make_asgi_app())
