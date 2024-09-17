GitHub API Automation Test

Этот проект позволяет автоматически тестировать работу с GitHub API: создавать, проверять и удалять репозиторий на GitHub с использованием Python.

Требования

    Операционная система: Windows, macOS или Linux
    Python: версия 3.10 или выше

Если у вас не установлен Python, следуйте шагам ниже, чтобы установить его.
Установка Python
Шаги для установки Python на Windows/macOS/Linux:

   1. Перейдите на официальный сайт Python и скачайте последнюю стабильную версию.
   2. Во время установки убедитесь, что выбрали опцию "Add Python to PATH" (Добавить Python в переменные среды).
   3. Проверьте установку, запустив в терминале/командной строке:
```bash
python --version
Должно появиться сообщение с номером версии Python
```
Настройка проекта
Шаг 1: Клонируйте репозиторий

Клонируйте этот репозиторий на свой компьютер:
```bash
git clone https://github.com/KoposOFF/Github-api.git
cd Githubapi
```
Шаг 2: Создайте и активируйте виртуальную среду

Рекомендуется использовать виртуальную среду для управления зависимостями проекта.
Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Для macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
После активации виртуальной среды вы увидите префикс (venv) перед командной строкой.

Шаг 3: Установите зависимости

Установите необходимые библиотеки, перечисленные в requirements.txt:
```bash
pip install -r requirements.txt
```
Шаг 4: Настройка переменных окружения

Перед запуском теста нужно настроить переменные окружения. Для этого создайте файл .env в корневой директории проекта.
```bash
    Создайте файл .env в корневом каталоге проекта.
    Добавьте в файл .env следующие переменные:
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=test-repo

```
GITHUB_USERNAME — ваше имя пользователя GitHub.
GITHUB_TOKEN — ваш токен доступа.
REPO_NAME — имя репозитория, который будет создан для теста.
GitHub Token (токен доступа) используется для аутентификации через GitHub API. Для его получения:

    Перейдите в GitHub Settings.
    Выберите Developer settings в левой боковой панели.
    Перейдите в Personal access tokens.
    Нажмите на Generate new token. Не забудьте включить права repo и delete_repo.
Пример :
GITHUB_USERNAME=Denis
GITHUB_TOKEN=ghp_1234567890abcdef
REPO_NAME=test-repo

Шаг 5: Запуск теста

Теперь вы можете запустить тест с помощью следующей команды:
```bash
python test_api.py
```
Если всё настроено правильно, скрипт создаст репозиторий на GitHub, проверит его наличие и удалит его.
