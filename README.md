
# Automatization framework to test Github servise 

<h3>Implemented Test Cases:</h3>
UI Tests web/ mobile platforms:

- [x]    Graphical user interface functionality (buttons, forms);
- [x]    Layout and element rendering;
- [x]    Client-side logic (e.g., field validation);

E2E Tests web platform:
- [x]    User scenaries of repository create;
- [x]    User scenaries of pull request create/ get/ update/ delete;

API Tests web platform:
- [x]    Issues CRUD operations;
- [x]    Data model and scheme validtion tests;

Project implemented using:

**Frameworks:**
  - Pytest
  - Selenium
  - Selene
  - Appium
  - Allure
  - pydantic
  - Faker

**Instruments:**
  - Jenkins
  - Allure Testops
  - Selenoid
  - Selenoid-UI
  - BrowserStack
  - Docker

Local Setup

    Clone the repository to your local machine using git clone

    Create and activate a virtual environment

bash

python -m venv .venv  
source .venv/bin/activate  # Linux/macOS  
.\.venv\Scripts\activate   # Windows  

    Install dependencies using pip

bash

pip install -r requirements.txt  

    To run tests locally, use:

bash

pytest .  

Generate Allure report:
bash

allure serve allure-results  

Remote Execution via Jenkins

    <a target="_blank" href="https://jenkins.autotests.cloud/job/litres-project/">Jenkins project link</a>

Build Parameters

These parameters are optional:

    ENVIRONMENT - defines the test environment (default: DEV)

    COMMENT - build comment

    BROWSER_NAME - browser for test execution (default: chrome)

    BROWSER_VERSION - browser version (default: 100.0)

https://resources/images/ui/jenkins_run.PNG
Running Tests in Jenkins
1. Open the <a target="_blank" href="https://jenkins.autotests.cloud/job/litres-project/">project</a>

https://resources/images/ui/jenkins.PNG
2. Select Build with Parameters
3. Modify build configuration if needed
4. Click Build
5. View results in Allure Report format
Allure Report
Overview

https://resources/images/ui/allure.PNG
Allure TestOps Integration

    <a target="_blank" href="https://allure.autotests.cloud/project/4083/dashboards">AllureTestOps project link</a> (access request: admin@qa.guru)

List of all test cases

https://resources/images/ui/allure_testops.PNG
Test run results

https://resources/images/ui/testops.PNG
Jira Integration

    <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1128">Jira project link</a>

https://resources/images/ui/jira.png
Telegram Notifications

https://resources/images/ui/telegram.PNG
Sample Test Execution Video

https://resources/images/ui/video.gif

TO-DO
[] Устойчивые локаторы
[] Ленивые элементы с улучшенным описанием для лучших отчетов
[] Паттерн "Wait for" для более стабильных тестов
[] Кастомные условия ожидания - расширение встроенных expected conditions
[//]: # ([] Абстрактный класс для пагеобжект)
[] Интеграция с Sentry для логирования ошибок
[] Проксирование запросов для анализа сетевой активности
[//]: # ([] Генерация тестовых данных на лету с помощью Faker)
[] Тестирование в разных ориентациях экрана
[] Интеграция с BrowserStack/Sauce Labs для облачного тестирования

[] PYTEST
pytest-xdist - для параллельного запуска тестов
pytest-rerunfailures - для перезапуска упавших тестов
pytest-html - для генерации HTML отчетов
pytest-allure - для красивых Allure отчетов
pytest-cov - для проверки покрытия кода тестами
