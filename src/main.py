from fastapi import FastAPI, HTTPException, status
from src.math_operation import add, sub, multiply, divide

app = FastAPI(
    title="FastAPI Math API",
    description="A simple API to perform basic math operations.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Root endpoint with a welcome message."""
    return {"message": "Welcome to the Math API. Visit /docs for documentation."}

@app.get("/add")
def api_add(a: float, b: float):
    """Adds two numbers provided as query parameters."""
    return {"operation": "add", "a": a, "b": b, "result": add(a, b)}

@app.get("/subtract")
def api_subtract(a: float, b: float):
    """Subtracts second number from the first."""
    return {"operation": "subtract", "a": a, "b": b, "result": sub(a, b)}

@app.get("/multiply")
def api_multiply(a: float, b: float):
    """Multiplies two numbers."""
    return {"operation": "multiply", "a": a, "b": b, "result": multiply(a, b)}

@app.get("/divide")
def api_divide(a: float, b: float):
    """
    Divides the first number by the second.
    Returns a 400 error if division by zero is attempted.
    """
    try:
        result = divide(a, b)
        return {"operation": "divide", "a": a, "b": b, "result": result}
    except ValueError as e:
        # Catch the specific error from our math function
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )