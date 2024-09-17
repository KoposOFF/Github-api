import os
import requests
from dotenv import load_dotenv

# Загрузка из .env
load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# URL для GitHub API
BASE_URL = 'https://api.github.com'
REPOS_URL = f'{BASE_URL}/user/repos'

# Функция для создания репозитория
def create_repo():
    response = requests.post(
        REPOS_URL,
        json={'name': REPO_NAME, 'private': False},
        headers={'Authorization': f'token {GITHUB_TOKEN}'}
    )
    response.raise_for_status()
    return response.json()

# Функция для проверки репозитория
def check_repo_exists():
    response = requests.get(
        REPOS_URL,
        headers={'Authorization': f'token {GITHUB_TOKEN}'}
    )
    response.raise_for_status()
    repos = response.json()
    return any(repo['name'] == REPO_NAME for repo in repos)

# Функция для удаления репозитория
def delete_repo():
    repo_url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(
        repo_url,
        headers={'Authorization': f'token {GITHUB_TOKEN}'}
    )
    response.raise_for_status()
    return response.status_code == 204

def test_github_api():
    print("Создание репозитория...")
    create_repo()
    assert check_repo_exists(), "Репозиторий не был создан"
    print("Репозиторий создан и проверен.")
    
    print("Удаление репозитория...")
    delete_repo()
    assert not check_repo_exists(), "Репозиторий не был удален"
    print("Репозиторий удален.")

if __name__ == '__main__':
    test_github_api()
