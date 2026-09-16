# Лабораторная работа №1

Самодуров Матвей Николаевич, группа 221341, вариант 8, лабораторная №1.

## Задания варианта

**Средняя сложность:**

- №8 — создать репозиторий на GitHub и связать его с локальным
- №10 — клонировать чужой репозиторий и изучить историю
- №4 — изменить файл, сделать второй коммит

**Повышенная сложность:**

- №8 — использовать git submodules
- №1 — разрешить конфликт при слиянии веток

## Клонирование

```bash
git clone --recurse-submodules https://github.com/<username>/mtp-lab1-variant8.git
cd mtp-lab1-variant8
```

Если репозиторий уже был клонирован без сабмодуля:

```bash
git submodule update --init --recursive
```

## Запуск

```bash
python -m lab1.repository_check
```

## Проверки

```bash
python -m unittest discover -s tests -v
python -m compileall -q lab1 tests
flake8 lab1 tests
```

Подробные доказательства выполнения собраны в каталоге `docs/`.
