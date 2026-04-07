import json
import os
import uuid
from datetime import datetime
from dataclasses import dataclass, asdict


DATA_FILE = "accounts.json"


@dataclass
class Account:
    account_id: str
    name: str
    email: str
    created_at: str


def _load_accounts() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_accounts(accounts: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=2)


def open_account(name: str, email: str) -> Account:
    accounts = _load_accounts()
    account_id = f"ACC-{str(len(accounts) + 1).zfill(4)}"
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account = Account(account_id=account_id, name=name, email=email, created_at=created_at)
    accounts.append(asdict(account))
    _save_accounts(accounts)
    return account
