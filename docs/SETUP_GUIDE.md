# 🚀 Setup Guide - SkinCare AI

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB RAM minimum
- Modern web browser

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Skin-Cancer-Prediction
```

### 2. Install Dependencies

```bash
cd webapp
pip install -r requirements.txt
```

### 3. Run Database Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Start the Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and visit:
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Project Structure

```
Skin-Cancer-Prediction/
├── webapp/              # Django web application
│   ├── APP/            # Main Django app
│   ├── PROJECT/        # Django settings
│   ├── templates/      # HTML templates
│   ├── static/         # CSS, JS, images
│   ├── media/          # User uploads
│   ├── models/         # ML model files
│   ├── scripts/        # Utility scripts
│   └── manage.py       # Django management
│
├── training/           # ML training
│   ├── data/          # Training datasets
│   ├── skin.ipynb     # Training notebook
│   └── SKIN CANCER.docx
│
├── docs/              # Documentation
└── README.md          # Quick start
```

## Configuration

### Database

The project uses SQLite by default. The database file is located at:
```
webapp/db.sqlite3
```

### Models

ML models are located at:
```
webapp/models/CNN_skin-cancer.h5
webapp/models/den_skin-cancer.h5
```

### Static Files

Static files are served from:
```
webapp/static/
```

### Media Files

User uploads are stored in:
```
webapp/media/
```

## Troubleshooting

### Port Already in Use

If port 8000 is already in use:
```bash
python manage.py runserver 8080
```

### Missing Dependencies

If you get import errors:
```bash
pip install -r requirements.txt --upgrade
```

### Database Errors

Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
```

### Model Not Found

Ensure model files exist in `webapp/models/`:
- CNN_skin-cancer.h5
- den_skin-cancer.h5

## Testing

### Run Performance Check

```bash
cd webapp
python scripts/performance_check.py
```

### Run Setup Check

```bash
cd webapp
python scripts/check_setup.py
```

## Development

### Running in Development Mode

```bash
cd webapp
python manage.py runserver
```

### Running in Production

See deployment documentation for production setup.

## Support

For issues and questions:
1. Check the documentation in `docs/`
2. Review the troubleshooting section
3. Check the project README.md

## Next Steps

After setup:
1. Create a user account
2. Upload a test image
3. View your analysis history
4. Explore the features

See [Testing Guide](TESTING_GUIDE.md) for comprehensive testing instructions.
