# Задача 3 — С подвохом: Шаблонизатор
#
# Напиши функцию render(template: str, **kwargs) -> str,
# которая подставляет переменные в шаблон — как .format(), но с дефолтами.
#
# Правила:
# - Шаблон содержит плейсхолдеры вида {name} или {name:default_value}
# - Если переменная передана в kwargs — подставить её
# - Если не передана, но есть default_value — подставить его
# - Если нет ни того, ни другого — оставить {name} как есть (не падать!)
#
# Примеры:
#   render("Hello, {name}!", name="Anton")        -> "Hello, Anton!"
#   render("Hello, {name:World}!")                -> "Hello, World!"
#   render("Hello, {name:World}!", name="Anton")  -> "Hello, Anton!"
#   render("Hello, {name}!")                      -> "Hello, {name}!"
#   render("{greeting:Hi}, {name}!", name="Anton") -> "Hi, Anton!"
#
# Подсказка: используй re.findall или str.format_map с кастомным dict
# Подвох: f-string здесь не поможет — шаблон приходит как строка в runtime

import re

class SafeDict(dict):
    def __missing__(self, key)-> str:
        return f"{{{key}}}"

def render(template: str, **kwargs) -> str:
    base_teplate = re.findall(r"\{([^}]+)\}", template)
    
    base_dict = {}
    
    for val in base_teplate:
        parts = val.split(":")
        if len(parts) > 1:
            base_dict[parts[0]] = parts[1]
            template = template.replace(val, parts[0])
        else:
            base_dict[val] = f"{{{val}}}"
    
    template = template.format_map(base_dict)
    
    if kwargs:
        return template.format_map(SafeDict(kwargs))
    
    return template



print(render("Hello, {name}!", name="Anton"))        
print(render("Hello, {name:World}!"))                
print(render("Hello, {name:World}!", name="Anton"))  
print(render("Hello, {name}!"))                      
print(render("{greeting:Hi}, {name}!", name="Anton"))
print(render("Hello, {name}!", age=30))