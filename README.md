# Face Detection App

A FastAPI-based application for face detection, recognition, and embedding management.

## Features

- **Face Embedding Creation**: Upload images to create facial embeddings for individuals
- **Face Comparison**: Compare two face images to determine similarity
- **Embedding Management**: Create, delete, and update facial embeddings
- **Database Storage**: Persistent storage of facial embeddings

## Project Structure

```
face_detection_app/
├── backend/
│   ├── db/
│   │   └── db.py                 # Database operations
│   ├── models/
│   │   ├── model.py              # Database models
│   │   └── schemas.py            # Pydantic schemas
│   ├── routes/
│   │   ├── auth.py               # Authentication routes
│   │   └── embeddings.py         # Face embedding routes
│   ├── utils/
│   │   └── face.py               # Face detection utilities
│   ├── uploads/                  # Uploaded images
│   ├── temp_images/              # Temporary image storage
│   ├── main.py                   # FastAPI application entry point
│   └── requirements.txt          # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd face_detection_app
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

### Face Embeddings
- `POST /create-embedding` - Create a facial embedding from an uploaded image
- `DELETE /delete-embedding` - Delete an existing embedding by person name
- `PUT /update-embedding` - Update an embedding (name change)

### Face Comparison
- `POST /compare-faces` - Compare two face images and return similarity score

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **OpenCV**: Computer vision library for face detection
- **NumPy**: Numerical computing library
- **SQLite**: Lightweight database for storing embeddings

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 