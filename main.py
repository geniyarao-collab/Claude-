from account import open_account


def main():
    account = open_account(name="みなみ", email="minami@example.com")
    print("アカウントを開設しました。")
    print(f"  名前      : {account.name}")
    print(f"  メール    : {account.email}")
    print(f"  アカウントID: {account.account_id}")
    print(f"  作成日時  : {account.created_at}")


if __name__ == "__main__":
    main()
