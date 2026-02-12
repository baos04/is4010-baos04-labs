def calculate_average_age(users: list) -> float:
    """Calculate the average numeric age from a list of user dicts.

    Non-numeric or missing ages are ignored. Returns 0.0 if no valid ages.
    """
    total = 0.0
    count = 0
    for u in users:
        try:
            age = u.get("age")
            if isinstance(age, (int, float)):
                total += float(age)
                count += 1
        except Exception:
            continue
    if count == 0:
        return 0.0
    return total / count


def get_active_user_emails(users: list) -> list:
    """Return list of emails for users with `is_active` truthy and an email present."""
    emails = []
    for u in users:
        try:
            if u.get("is_active") and "email" in u and isinstance(u.get("email"), str):
                emails.append(u.get("email"))
        except Exception:
            continue
    return emails
