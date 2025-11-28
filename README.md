# Flask Faculty Locator

This is a simple Flask web application that allows users to search faculty details stored in a SQLite database and view basic information such as department, block, floor, and cabin number.

## Features

- SQLite database (`faculty.db`) created and seeded using `db.py`.
- REST API to fetch all faculty records as JSON.
- REST API to fetch a single faculty record by ID as JSON.
- Web interface to search faculty by name and display results.

## Project Structure

```
.
├─ db.py              # Creates faculty.db and inserts sample data
├─ main.py            # Flask application (routes, API, search)
├─ requirements.txt   # Python dependencies (Flask, etc.)
└─ templates/
   ├─ index.html      # Search form page
   └─ result.html     # Search results page
```

## Getting Started

### 1. Clone or download this repository

If you have Git installed:

```
git clone https://github.com/MadhurimaKumari/Faculty-Finder.git
cd Faculty-Finder
```

Or download the ZIP from GitHub and extract it.

### 2. Create and activate a virtual environment (optional but recommended)

```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

Make sure you have `pip` installed, then run:

```
pip install -r requirements.txt
```

If you don't want to use `requirements.txt`, you can install Flask directly:

```
pip install flask
```

### 4. Initialize the database

Run `db.py` once to create the SQLite database and insert sample faculty data:

```
python db.py
```

This will create a file named `faculty.db` in the project directory.

### 5. Run the Flask application

Start the development server with:

```
python main.py
```

By default, the app runs at:

- Home page: http://127.0.0.1:5000/
- Search endpoint: `/search`
- API endpoints:
  - `GET /api/faculty` – returns all faculty as JSON
  - `GET /api/faculty/<id>` – returns a single faculty record by ID as JSON

Open your browser and visit:

```
http://127.0.0.1:5000/
```

### 6. Usage

- On the home page, enter a faculty name (or part of the name) into the search box.
- Submit the form to see matching faculty records with their department, block, floor, and cabin number.

## Files Overview

### db.py

- Connects to `faculty.db`.
- Creates a `faculty` table if it does not exist.
- Inserts some sample faculty rows.
- Commits and closes the connection.

Run this file once before using the app.

### main.py

- Sets up the Flask app and database connection helper.
- `/` route: renders `index.html`.
- `/api/faculty`: returns all faculty records as JSON.
- `/api/faculty/<id>`: returns one faculty record by ID as JSON or a 404 JSON error if not found.
- `/search`: reads the `q` query parameter, searches by `name` using a `LIKE` query, and renders `result.html` with results.

## requirements.txt

Example contents :

```
Flask==3.0.0
```

## Sample Data Available for Testing

The application comes preloaded with the following faculty records.  
Use these values in the search bar to test how the system works:

| ID | Name   | Department | Block | Floor | Cabin No |
|----|--------|------------|-------|--------|-----------|
| 1  | Anil   | CSE        | A     | 2      | 101       |
| 2  | Ram    | AI-ML      | AI    | 2      | 101       |
| 3  | Sunil  | CSE        | A     | 3      | 112       |
| 4  | Mohan  | Law        | B     | 1      | 123       |
| 5  | Sohan  | CSE        | A     | 2      | 103       |

### Example searches:
- By Name: "Anil", "Ram", "Sunil", "ohan", "an", "il"


## Future Enhancements

- Admin panel
- Bootstrap UI
- Autocomplete search
- Campus map
- Mobile responsive layout
- Search by Department, ID, position, Floor, Block
- Filters on Roles, Department, position

