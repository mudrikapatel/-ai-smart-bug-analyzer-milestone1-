def analyze_root_cause(text):

    text = text.lower()

    if "nullpointerexception" in text:
        return {
            "cause": "A null object was accessed before initialization.",
            "confidence": 96,
            "evidence": "NullPointerException detected in the stack trace.",
            "recommendation": "Initialize the object or add null checks before accessing its methods."
        }

    elif "sql" in text or "sqlexception" in text:
        return {
            "cause": "Database query execution failed.",
            "confidence": 93,
            "evidence": "SQL exception detected.",
            "recommendation": "Validate SQL queries and database connection."
        }

    elif "sockettimeoutexception" in text or "timeout" in text:
        return {
            "cause": "The application timed out while waiting for a response.",
            "confidence": 91,
            "evidence": "Timeout exception detected.",
            "recommendation": "Optimize the backend service or increase timeout settings."
        }

    elif "filenotfoundexception" in text:
        return {
            "cause": "The application could not find the required file.",
            "confidence": 94,
            "evidence": "FileNotFoundException detected.",
            "recommendation": "Verify the file path and ensure the file exists."
        }

    else:
        return {
            "cause": "Application crashed due to an unhandled runtime exception.",
            "confidence": 72,
            "evidence": "No known exception pattern matched.",
            "recommendation": "Review logs and inspect the failing module."
        }