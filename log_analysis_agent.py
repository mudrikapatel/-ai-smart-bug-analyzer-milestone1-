import re

def analyze_log(text):

    text_lower = text.lower()

    result = {
        "exception": "Unknown",
        "failure_point": "Unknown",
        "code_path": "Unknown",
        "message": text.strip()
    }

    # -----------------------
    # Detect Exception
    # -----------------------

    if "nullpointerexception" in text_lower:
        result["exception"] = "NullPointerException"

    elif "sql" in text_lower:
        result["exception"] = "SQLException"

    elif "timeout" in text_lower:
        result["exception"] = "TimeoutException"

    elif "index out of bounds" in text_lower:
        result["exception"] = "IndexOutOfBoundsException"

    elif "file not found" in text_lower:
        result["exception"] = "FileNotFoundException"

    elif "crash" in text_lower:
        result["exception"] = "Runtime Crash"

    elif "api" in text_lower and "500" in text_lower:
        result["exception"] = "HTTP 500 Internal Server Error"

    # -----------------------
    # Failure Point
    # -----------------------

    if "login" in text_lower:
        result["failure_point"] = "Login Module"

    elif "database" in text_lower:
        result["failure_point"] = "Database Layer"

    elif "api" in text_lower:
        result["failure_point"] = "API Endpoint"

    elif "payment" in text_lower:
        result["failure_point"] = "Payment Module"

    elif "dashboard" in text_lower:
        result["failure_point"] = "Dashboard"

    # -----------------------
    # Code Path
    # -----------------------

    if "login" in text_lower:
        result["code_path"] = "LoginService.authenticate()"

    elif "database" in text_lower:
        result["code_path"] = "Database.connect()"

    elif "api" in text_lower:
        result["code_path"] = "APIController.handleRequest()"

    elif "payment" in text_lower:
        result["code_path"] = "PaymentService.processPayment()"

    return result