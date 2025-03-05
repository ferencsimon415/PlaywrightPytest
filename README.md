# Playwright-Pytest Automation Framework

This project provides a robust and scalable framework for web automation testing using Playwright and Pytest. It's designed to make it easy to write, run, and manage UI and API tests, and it integrates seamlessly with Allure for comprehensive reporting.

## Key Features

*   **Web Automation:** Utilizes Playwright for reliable and cross-browser web automation.
*   **Test Framework:** Leverages Pytest for test discovery, execution, and powerful fixture management.
*   **Comprehensive Reporting:** Integrates with Allure for detailed, interactive test reports.
*   **API Testing:** Supports API testing with request/response logging.
*   **Data-Driven Testing:** Includes mechanisms for loading test data from JSON files.
*   **Configuration Management:** Uses a `Config` module to manage base URLs, browser settings, and other configurations.
*   **Screenshot on Failure:** Automatically captures screenshots when UI tests fail, providing visual debugging assistance.
*   **Request/Response Logging:** Captures and logs request and response details for all API interactions, regardless of the test status.
*   **Organized Structure:** Follows a clear structure for tests, data, configurations, and page objects.
*   **Clear separation** of ui and api tests.


## Getting Started

### Prerequisites

*   **Python 3.8+**
*   **pip** (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd PlaywrightPytest
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    # Activate the virtual environment:
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    If you don't have the `requirements.txt` file, execute `pip install playwright pytest allure-pytest requests`

4. **Install playwright browser:**

```bash
playwright install
