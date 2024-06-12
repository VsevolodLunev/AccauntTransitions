import datetime from datetime
from functions import load_operations, mask_cart_number, mask_acc, get_operations


def main():
    for operation in get_operations(load_operations()):
        date = datetime.fromisoformat(operation["date"]).strftimestrftime("%d/%m/%Y")
        description = operation.get("description", '')
        from_acc = operation.get("from", '')
        to_acc = operation.get("to", '')


if __name__ == '__main__':
    main()