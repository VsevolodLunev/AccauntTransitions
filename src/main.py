from  datetime import datetime
from src.functions import load_operations, mask_cart_number, mask_acc, get_operations


def main():
    for operation in get_operations(load_operations()):
        date = datetime.fromisoformat(operation["date"]).strftime("%d.%m.%Y")
        description = operation.get("description", '')
        from_acc = operation.get("from", '')
        to_acc = operation.get("to", '')

        if 'Счет' in from_acc:
            from_acc = f"Счет {mask_acc(from_acc)}"
        else:
            from_acc = mask_cart_number(from_acc)

        if 'Счет' in to_acc:
            to_acc = f"Счет {mask_acc(to_acc)}"
        else:
            to_acc = mask_cart_number(to_acc)

        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        if operation["description"] == "Открытие вклада":
            print(f'''{date} {description}
-> {to_acc}
{amount} {currency}
''')
        else:
            print(f'''{date} {description}
{from_acc} -> {to_acc}
{amount} {currency}
''')



if __name__ == '__main__':
    main()