# ScheduleApp - Мобильное приложение для просмотра расписания

ScheduleApp - это мобильное приложение для Android, разработанное на Python с использованием фреймворка KivyMD для отображения учебного расписания студентов [1](#0-0) . Приложение позволяет просматривать ежедневное расписание занятий с возможностью навигации между днями недели [2](#0-1) .

## Основные возможности

- **Просмотр расписания по дням**: Отображение расписания занятий для каждого дня недели с информацией о предмете, преподавателе и аудитории [3](#0-2) 
- **Навигация**: Переключение между днями с помощью кнопок "влево" и "вправо" [4](#0-3) 
- **Поддержка чередующихся недель**: Автоматическое определение четной/нечетной недели для отображения соответствующего расписания [5](#0-4) 
- **Material Design интерфейс**: Современный пользовательский интерфейс на основе KivyMD [6](#0-5) 

## Технические характеристики

- **Язык разработки**: Python 3
- **UI Framework**: KivyMD (Material Design для Kivy) [7](#0-6) 
- **Платформа**: Android (ARM64, ARMv7) <cite />
- **Система сборки**: Buildozer для создания APK файлов [8](#0-7) 

## Структура проекта

```
ScheduleApp/
├── main.py              # Основная логика приложения
├── schedule.kv          # UI разметка в формате Kivy
├── shedule/            # Модуль с данными расписания
│   ├── __init__.py
│   └── shedule.py      # Словарь с расписанием занятий
└── buildozer.spec      # Конфигурация для сборки Android APK
```

## Архитектура

Приложение построено по принципу разделения ответственности:
- **Слой представления**: Декларативный UI в файле `schedule.kv` [9](#0-8) 
- **Слой логики**: Класс `ScheduleApp` управляет состоянием и обработкой событий [10](#0-9) 
- **Слой данных**: Структурированное хранение расписания в `schedule_dict` [11](#0-10) 

## Установка и запуск

Для сборки Android APK используется Buildozer:
```bash
buildozer android debug
```

Приложение поддерживает портретную ориентацию и оптимизировано для мобильных устройств [12](#0-11) .

## Notes

Приложение содержит расписание для студентов с занятиями по различным предметам включая математический анализ, физику, химию, иностранные языки и другие дисциплины. Данные расписания хранятся в структурированном формате с поддержкой чередования по неделям для некоторых предметов, особенно заметно в пятничном расписании где есть различия между четными и нечетными неделями.

Wiki pages you might want to explore:
- [System Architecture (darkyz12345/ScheduleApp)](/wiki/darkyz12345/ScheduleApp#2)

### Citations

**File:** main.py (L1-8)
```python
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText


from datetime import datetime, timedelta
from calendar import day_name
from shedule.shedule import schedule_dict
```

**File:** main.py (L14-18)
```python
class ScheduleApp(MDApp):
    def __init__(self):
        self.date = datetime.now()
        self.day = self.date.strftime('%A').upper()
        super(ScheduleApp, self).__init__()
```

**File:** main.py (L27-37)
```python
    def left_arrow_btn(self):
        self.date -= timedelta(days=1)
        self.day = self.date.strftime('%A').upper()
        self.root.ids.month_lbl.text = self.day
        self.update_list()

    def right_arrow_btn(self):
        self.date += timedelta(days=1)
        self.day = self.date.strftime('%A').upper()
        self.root.ids.month_lbl.text = self.day
        self.update_list()
```

**File:** main.py (L43-43)
```python
            ind = self.date.isocalendar()[1] % 2
```

**File:** main.py (L45-51)
```python
            for key, value in schedule.items():
                object = value['object'][ind]
                name_teacher = value['name_teacher'][ind]
                room = value['room'][ind]
                list_items.append(MDListItem(MDListItemHeadlineText(text=object),
                                             MDListItemSupportingText(text=name_teacher),
                                             MDListItemTertiaryText(text=room)))
```

**File:** schedule.kv (L1-3)
```text
MDBoxLayout:
    md_bg_color: app.theme_cls.surfaceColor
    orientation: 'vertical'
```

**File:** schedule.kv (L24-25)
```text
            MDList:
                id: schedule_list
```

**File:** schedule.kv (L28-45)
```text
        MDButton:
            id: left_button
            style: "elevated"
            theme_width: "Custom"
            size_hint_x: .5

            MDButtonIcon:
                icon: "arrow-left-bold"
                pos_hint: {"center_x": .5, "center_y": .5}
        MDButton:
            id: right_button
            style: "elevated"
            theme_width: "Custom"
            size_hint_x: .5

            MDButtonIcon:
                icon: "arrow-right-bold"
```

**File:** buildozer.spec (L1-10)
```text
[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test
```

**File:** buildozer.spec (L60-60)
```text
orientation = portrait
```

**File:** shedule/shedule.py (L1-10)
```python
schedule_dict: dict[str, dict[str, dict[str, list[str] | str]]] = {
    'monday': {'09:00-10:20': {'object': ['Химия (лек)'] * 2,
                               'name_teacher': ['Мухтаров О.П.'] * 2,
                               'room': ['104'] * 2},
               '10:20-11:50': {'object': ['Физическая культура'] * 2,
                               'name_teacher': ['Сияев С.'] * 2,
                               'room': ['спортзал'] * 2},
               '12:40-14:00': {'object': ['Иностранный язык (английский)'] * 2,
                               'name_teacher': ['Мухаммадиева Ш.Г.'] * 2,
                               'room': ['216'] * 2}},
```
