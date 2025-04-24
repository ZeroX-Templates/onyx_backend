# scanner.py
import re

def scan_secrets(content: str):
    # Simple regex pattern to detect common API keys, tokens, etc.
    patterns = [
        r'(?<=api_key=)[A-Za-z0-9_-]+',
        r'(?<=token=)[A-Za-z0-9_-]+',
        r'(?<=secret=)[A-Za-z0-9_-]+',
    ]
    secrets = []
    for pattern in patterns:
        found = re.findall(pattern, content)
        secrets.extend(found)
    return secrets
