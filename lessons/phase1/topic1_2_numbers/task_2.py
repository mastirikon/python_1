from decimal import Decimal, ROUND_HALF_UP

def split_bill(total_str: str, people: int) -> str:
    return str((Decimal(total_str) / people).quantize(Decimal("0.01"), ROUND_HALF_UP))

result = split_bill("100.00", 3)

print(result)