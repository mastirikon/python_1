from decimal import ROUND_HALF_UP, Decimal

def format_price(amount: float, currency: str = "USD") -> str:
    dec_amount: Decimal = Decimal(str(amount))
    rounded = dec_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return f"{rounded} {currency}"

print(format_price(19.99))
print(format_price(19.987))