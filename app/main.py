from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def get_reference():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url, title="SupportIQ API Reference"
    )
