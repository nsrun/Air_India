

A Django-based web application that serves as a clone/redesign of the Air India website. This project includes flight booking, user authentication, and informational pages structured to mirror a professional airline portal.

## Features

- **User Authentication:** Sign up and log in functionality for users.
- **Flight Booking:** Interfaces and models to support searching and booking flights.
- **Modern UI:** Styled templates including Home, About, Bookings, and specific flight booking pages to provide a premium user experience.

## Project Structure

- `airIndia1/`: Main Django project configuration directory.
- `flight/`: Django app containing models, views, and logic for flight-related operations.
- `templates/`: HTML templates for the frontend UI.
- `manage.py`: Django's command-line utility for administrative tasks.
- `db.sqlite3`: Default SQLite database.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd airIndia1
   ```

2. **Install dependencies:**
   Ensure you have Python and Django installed. You can install Django via pip:
   ```bash
   pip install django
   ```
   *(Note: If a `requirements.txt` is present, use `pip install -r requirements.txt`)*

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

Navigate through the website to explore the various pages like Home, About, and Bookings. You can create an account or sign in to access personalized features.
