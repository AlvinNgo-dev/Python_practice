import re


def replace_emails(text):
    # Regex pattern for email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Replace all emails with a placeholder
    replaced_text = re.sub(pattern, '[EMAIL]', text)

    return replaced_text


# Example usage
text = "Contact us at support@example.com or admin@test.org for more info."
result = replace_emails(text)
print(result)
