# Отчёт о клонировании внешнего репозитория

## Репозиторий

- **URL**: https://github.com/pypa/sampleproject.git
- **Описание**: Sample project from the Python Packaging Authority (PyPA)
- **Клонирование**:

```bash
git clone https://github.com/pypa/sampleproject.git
```

## Изучение истории

### Удалённые адреса

```
origin	git@github.com:pypa/sampleproject.git (fetch)
origin	git@github.com:pypa/sampleproject.git (push)
```

### Общее количество коммитов

```
git rev-list --count HEAD
197
```

### Ветки

```
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

Только одна ветка — main. Тегов нет.

### Последние 10 коммитов

```
621e497 pyproject: prep 4.0.0 (#219)
8603eaf Update workflow actions to remove warning messages (#214)
a1f0005 Switch to `nox` for automated testing (#212)
5d27795 Update pyproject.toml (#204)
b1dfa48 Fixes inconsistencies in pyproject.toml documentation. (#197)
9944026 update python versions (#207)
3fb1461 Update `release.yml` with release branch for `gh-action-pypi-publish` (#195)
bae8ff4 Add token permissions to release workflow. (#192)
fc8d83e Update `release.yml` to use Trusted Publishing (#191)
fa13f7d Remove workflow warnings (#190)
```

### Первые 5 коммитов

```
215d8d6 | 2013-12-03 | Paul Moore | Initial commit
6979a8d | 2013-12-03 | Paul Moore | Tidy up setup.py and add the mandatory url parameter
ec93951 | 2013-12-03 | Paul Moore | Read the __init__.py file directly to get the package version
0ebe2d9 | 2013-12-03 | Paul Moore | Add a MANIFEST.in to ensure support files are in the sdist
bc70c6f | 2014-02-22 | Marcus Smith | give README an rst extension
```

### Самые активные авторы (без merge-коммитов)

```
    26	Marcus Smith
    25	Dustin Ingram
     9	Paul Moore
     6	Ryan Long
     4	Marcel Martin
     3	Dan Søndergaard
     3	Matt Iversen
     3	Philip James
     3	Rebecca Turner
     2	David Tucker
```

### Merge-коммиты

```
git log --merges --oneline | wc -l
58
```

### Выводы

- Репозиторий существует с 3 декабря 2013 года (первый коммит Paul Moore).
- Последний коммит: 6 ноября 2024 года (William Woodruff).
- 197 коммитов, из них 58 — merge-коммиты (через Pull Request).
- Единственная ветка — main; тегов нет, версии фиксируются коммитами.
- Самые активные авторы — Marcus Smith (26) и Dustin Ingram (25).
- Изменения попадают через Pull Request.
