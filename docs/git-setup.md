# Настройка Git

Используемая версия:

```text
git version 2.47.2
```

Локальная конфигурация репозитория:

```bash
git config --local user.name "Samodurov Matvey"
git config --local user.email "matvey.samodurov@example.com"
```

Проверка:

```text
$ git config --local --get user.name
Samodurov Matvey

$ git config --local --get user.email
matvey.samodurov@example.com
```

Проверка автора коммитов:

```bash
git log --format="%h %an <%ae> %s"
```

```text
40de3db Samodurov Matvey <matvey.samodurov@example.com> feat: add file counting utility to repository check
9063b43 Samodurov Matvey <matvey.samodurov@example.com> docs: create initial project skeleton
```
