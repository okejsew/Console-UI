# Console-UI

`Console-UI` — это библиотека для создания пользовательских интерфейсов в консоли на Python с использованием библиотеки `curses`. Библиотека вдохновлена WinForms и предоставляет возможность работы с различными контролами: кнопки, слайдеры, чекбоксы, текстовые поля и многое другое.

## Возможности
- **Создание окон:** Поддержка переключения между окнами.
- **Контролы:**
  - Кнопки (`Button`)
  - Чекбоксы (`Checkbox`)
  - Выпадающие списки (`Dropdown`)
  - Метки (`Label`)
  - Прогресс-бары (`ProgressBar`)
  - Слайдеры (`Slider`)
  - Текстовые поля (`TextBox`)
- **События:**
  - Нажатие клавиш
  - Клик мыши
  - Наведение/уход мыши

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/console-ui.git
   ```

2. Перейдите в директорию проекта и установите библиотеку:
   ```bash
   cd console-ui
   pip install .
   ```

Или установите через `pip` после публикации:
   ```bash
   pip install console-ui
   ```

## Быстрый старт

Пример использования библиотеки для создания окна с кнопкой и чекбоксом:

```python
from console import ConsoleWindow
from console.controls.button import Button
from console.controls.checkbox import Checkbox

def main():
    # Создаем окно
    window = ConsoleWindow()

    # Добавляем кнопку
    button = Button()
    button.text = "Click Me!"
    button.location.x, button.location.y = 5, 2
    window.add(button)

    # Добавляем чекбокс
    checkbox = Checkbox()
    checkbox.text = "I agree"
    checkbox.location.x, checkbox.location.y = 5, 5
    window.add(checkbox)

    # Отображаем окно
    window.show()

if __name__ == "__main__":
    main()
```

## Описание контролов

### 1. `Button`
- **Описание:** Простая кнопка, которая может реагировать на события мыши.
- **Настройки:**
  - `text`: текст на кнопке.

Пример:
```python
button = Button()
button.text = "Submit"
button.location.x, button.location.y = 2, 3
```

---

### 2. `Checkbox`
- **Описание:** Чекбокс с возможностью переключения.
- **Настройки:**
  - `text`: текст рядом с чекбоксом.
  - `checked`: `True`/`False` — состояние чекбокса.

Пример:
```python
checkbox = Checkbox()
checkbox.text = "Accept Terms"
checkbox.checked = True
checkbox.location.x, checkbox.location.y = 4, 6
```

---

### 3. `Dropdown`
- **Описание:** Выпадающий список с элементами.
- **Настройки:**
  - `items`: список элементов.
  - `width`: ширина видимой области.
  - `max_drop`: количество отображаемых элементов.

Пример:
```python
dropdown = Dropdown()
dropdown.items = ["Option 1", "Option 2", "Option 3"]
dropdown.location.x, dropdown.location.y = 8, 4
```

---

### 4. `Label`
- **Описание:** Текстовая метка.
- **Настройки:**
  - `text`: текст метки.

Пример:
```python
label = Label()
label.text = "Hello, World!"
label.location.x, label.location.y = 0, 0
```

---

### 5. `ProgressBar`
- **Описание:** Прогресс-бар для отображения выполнения задачи.
- **Настройки:**
  - `value`: текущее значение.
  - `max_value`: максимальное значение.
  - `width`: ширина прогресс-бара.

Пример:
```python
progress = ProgressBar()
progress.value = 5
progress.max_value = 10
progress.location.x, progress.location.y = 10, 2
```

---

### 6. `Slider`
- **Описание:** Ползунок, основанный на `ProgressBar`.
- **Настройки:** Те же, что и у `ProgressBar`, плюс:
  - Поддержка управления мышью и клавишами.

Пример:
```python
slider = Slider()
slider.value = 3
slider.max_value = 10
slider.location.x, slider.location.y = 12, 4
```

---

### 7. `TextBox`
- **Описание:** Поле для ввода текста.
- **Настройки:**
  - `text`: текущий текст.
  - `title`: заголовок поля.
  - `placeholder`: текст-подсказка.

Пример:
```python
textbox = TextBox()
textbox.title = "Input"
textbox.placeholder = "Enter your name"
textbox.location.x, textbox.location.y = 15, 5
```

---

## Требования
- Python 3.6+
- `curses` (встроена в стандартную библиотеку Python на Unix-подобных системах).
- `windows-curses` если вы на Windows
