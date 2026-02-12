import importlib.util
import os

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("lab05", os.path.join(here, "lab05.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def run_checks():
    sample_users = [
        {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "is_active": False},
        {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
        {"name": "david", "age": "unknown", "is_active": False},
        {"name": "eve", "is_active": True, "email": "eve@example.com"},
    ]

    assert mod.calculate_average_age(sample_users) == 30.0
    assert mod.calculate_average_age([]) == 0.0

    expected = {"alice@example.com", "charlie@example.com", "eve@example.com"}
    assert set(mod.get_active_user_emails(sample_users)) == expected
    assert mod.get_active_user_emails([{"name": "bob", "age": 25, "is_active": False}]) == []
    assert mod.get_active_user_emails([]) == []

    print("All lab05 checks passed")

if __name__ == '__main__':
    run_checks()
