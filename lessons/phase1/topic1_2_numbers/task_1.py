def hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return f"{hours}h {minutes}m {seconds}s"

data = 3725
print(data)
result = hms(3725)
print(result)
print(data)