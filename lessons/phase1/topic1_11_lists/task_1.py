# Задача 1 — Лёгкая: Стек истории
#
# Напиши класс BrowserHistory, который симулирует историю браузера:
# - visit(url: str) — добавить страницу в историю
# - back() -> str | None — вернуться назад (удалить и вернуть текущую),
#   если история пуста — вернуть None
# - current() -> str | None — текущая страница (последняя в истории)
# - history() -> list — вся история в порядке посещения
#
# Пример:
#   bh = BrowserHistory()
#   bh.visit("google.com")
#   bh.visit("github.com")
#   bh.visit("docs.python.org")
#   print(bh.current())   # docs.python.org
#   print(bh.back())      # docs.python.org
#   print(bh.current())   # github.com
#   print(bh.history())   # ['google.com', 'github.com']

class BrowserHistory:
    def __init__(self):
        self._history: list[str] = []
    
    def visit(self, url: str) -> None:
        self._history.append(url)
    
    def back(self) -> str | None:
        return self._history.pop() if self._history else None
    
    def current(self) -> str | None:
        return self._history[-1] if self._history else None
    
    def history(self) -> list:
        return self._history


bh = BrowserHistory()
bh.visit("google.com")
bh.visit("github.com")
bh.visit("docs.python.org")
print(bh.current())   # docs.python.org
print(bh.back())      # docs.python.org
print(bh.current())   # github.com
print(bh.history())   # ['google.com', 'github.com']