# Office Management System

## Overview

The Office Management System is a web application designed to streamline the process of managing employee details. Built with Django, Python, Bootstrap, HTML, CSS, JavaScript, and MySQL, it provides features such as adding, removing, viewing, and filtering employee details. It also includes email OTP authentication for new managers.

## Features

- **Add Employee Details:** Managers can add new employee details to the system.
- **Remove Employee Details:** Managers can remove existing employee details.
- **View Employee Details:** Managers can view details of all employees.
- **Filter Employee Details:** Managers can filter employee details based on different criteria.
- **Email OTP Authentication:** New managers are authenticated via an email OTP system.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** Bootstrap, HTML, CSS, JavaScript
- **Database:** MySQL

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or later
- MySQL
- Node.js and npm (for managing JavaScript dependencies)

### Installation

1. **Clone the repository:**
    ```sh
    git clonehttps://github.com/Roshanhaurasia9319/Office-management-system
    cd office-emp-proj
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv myworld
    source myworld/Scripts/Activate
    ```

3. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```


4. **Setup MySQL Database:**
    - Create a MySQL database and update the `DATABASES` settings in `settings.py`:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your-database-name',
                'USER': 'your-database-user',
                'PASSWORD': 'your-database-password',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```

5. **Run Database Migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Development Server:**
    ```sh
    python manage.py runserver
    ```

7. **Open the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Adding Employee Details
1. Log in as a manager.
2. Navigate to the "Add Employee" section.
3. Fill out the employee details form and submit.

### Removing Employee Details
1. Log in as a manager.
2. Navigate to the "Employee List" section.
3. Select the employee to be removed and confirm the action.

### Viewing Employee Details
1. Log in as a manager.
2. Navigate to the "Employee List" section to view all employee details.

### Filtering Employee Details
1. Log in as a manager.
2. Use the filter options in the "Employee List" section to filter employee details based on different criteria.

### Authenticating New Managers
1. New managers sign up using their email address.
2. An OTP is sent to the provided email for authentication.
3. Enter the OTP to complete the authentication process.



