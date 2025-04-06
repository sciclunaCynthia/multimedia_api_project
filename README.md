# multimedia_api_project for Database Essensials Assignment

## Folder Structure
multimedia_api_project/
│
├── main.py                  # Main FastAPI application with all endpoints
├── requirements.txt         # Python dependencies for the app (e.g., FastAPI, motor)
├── vercel.json              # Vercel config to run the FastAPI app as a serverless function
├── .gitignore               # Files/folders to ignore in version control
├── README.md                
│
├── multimedia_api_project/  # (subfolder containing env files)
│
└── screenshots/             # Saved screenshots for documentation/testing

## Features

- Upload `.png`, `.jpg` (sprite) files via `/upload_sprite`
- Upload `.wav` or `.mp3` (audio) files via `/upload_audio`
- Submit player score via `/player_score` (name + score)
- Data is stored in MongoDB Atlas
- Swagger UI available at `/docs`

## Security

- Uses password-authenticated MongoDB user
- IP whitelisting set up via MongoDB Atlas
- Input validated via Pydantic + custom sanitation

##  How to Test

Visit the Swagger UI (Vercel deployed) via the link below:

- https://multimedia-api-project-cynthia.vercel.app/docs

Use the interface to:
- Upload an image file
- Upload an audio file
- Submit a score with a name

It will show a 200 ok status code indicating that the endpoint works and the API is functioning properly

## Technologies Used

- Python 3.12
- FastAPI
- MongoDB Atlas (via `motor`)
- Swagger UI (built-in with FastAPI)
- Vercel for deployment

## Screenshots 
Check the `/screenshots` folder for the screenshots used for testing and documentation