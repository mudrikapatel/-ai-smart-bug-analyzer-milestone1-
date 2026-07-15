def analyze_bug(text):
    text = text.lower()

    severity = "Low"
    priority = "P3"
    component = "General"
    confidence = 75
    reasoning = "General bug report."

    if "crash" in text or "exception" in text or "fatal" in text:
        severity = "Critical"
        priority = "P1"
        confidence = 98
        reasoning = "Runtime exception or application crash detected."

    elif "login" in text:
        severity = "High"
        priority = "P1"
        component = "Authentication"
        confidence = 95
        reasoning = "Authentication failure detected."

    elif "database" in text or "sql" in text:
        severity = "High"
        priority = "P1"
        component = "Database"
        confidence = 92
        reasoning = "Database-related issue detected."

    elif "api" in text:
        severity = "Medium"
        priority = "P2"
        component = "API"
        confidence = 88
        reasoning = "API endpoint issue detected."

    elif "ui" in text or "button" in text:
        severity = "Low"
        priority = "P3"
        component = "Frontend"
        confidence = 85
        reasoning = "User interface issue detected."

    return {
        "severity": severity,
        "priority": priority,
        "component": component,
        "confidence": confidence,
        "reasoning": reasoning
    }