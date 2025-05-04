# Events App

The Events App is a web application that allows users to create, view, and RSVP to events. It also provides functionality to view guest details and manage event attendees. A default event is preloaded for first-time users to explore the app.

## Features
- Create new events with a title, description, date, and time.
- View a list of all events.
- RSVP to events as a new or returning guest.
- View details of individual events, including attendees.
- View details of individual guests, including the events they are attending.

## Setup Instructions

### 1. Clone the Repository
Start by cloning this repository to your computer:
```
git clone https://github.com/YogiSunil/Events_HW.git
```

### 3. Install Dependencies
Install the required Python packages:
```
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```
python app.py
```

### 5. Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Notes
- A default event titled "Welcome Event" is preloaded for first-time users.
- The application uses SQLite as the database backend.
- Ensure Python 3.7 or higher is installed on your system.

## Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes.