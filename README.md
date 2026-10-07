# Veri Snap

A Streamlit-based application for intelligent student attendance and enrollment management using face recognition and voice analysis.

## Features

- **Face Recognition**: Automated attendance tracking using facial recognition technology
- **Voice Attendance**: Alternative attendance marking via voice recognition
- **Student Management**: Easy enrollment, subject assignment, and student profile management
- **Teacher Dashboard**: Comprehensive view of classes, attendance records, and student data
- **QR Code Integration**: Generate QR codes for quick enrollment and sharing
- **Database Integration**: Supabase backend for secure data storage
- **Real-time Dialogue UI**: Interactive components for smooth user experience

## Project Structure

```
Veri Snap/
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Runtime configuration
├── .gitignore                  # Git ignore rules
│
├── src/
│   ├── components/             # Reusable UI components
│   │   ├── dialogue_add_photo.py
│   │   ├── dialogue_attendance_results.py
│   │   ├── dialogue_auto_enroll.py
│   │   ├── dialogue_create_subject.py
│   │   ├── dialogue_enroll.py
│   │   ├── dialogue_share_subject.py
│   │   ├── dialogue_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database/               # Database configuration and operations
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines/              # ML pipelines for recognition
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens/                # Application screens/pages
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui/                     # UI utilities
│       └── base_layout.py
│
└── vendor/                     # Third-party packages
    └── webrtcvad_compat/
```

## Installation

### Prerequisites
- Python 3.12 or higher
- Virtual environment manager (venv, conda, etc.)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Smart\ Snap
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv312
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .\venv312\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv312/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your Supabase credentials and other configuration:
     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_key
     ```

## Running the Application

```bash
streamlit run app.py
```

The application will start and be accessible at `http://localhost:8501`

## Technologies Used

- **Frontend**: Streamlit - Python web app framework
- **Face Recognition**: dlib, face_recognition library
- **Voice Recognition**: Librosa, WebRTC VAD, Resemblyzer
- **Machine Learning**: scikit-learn (SVM classifier)
- **Database**: Supabase (PostgreSQL)
- **Image Processing**: Pillow
- **QR Codes**: Segno
- **Audio Processing**: Librosa

## Key Features Explained

### Face Recognition Pipeline
- Detects faces in images using dlib
- Extracts 128-dimensional face embeddings
- Trains an SVM classifier on student embeddings
- Matches new faces against the trained model

### Voice Attendance
- Processes audio input for voice analysis
- Uses WebRTC VAD for voice activity detection
- Analyzes voice characteristics for identification

### Database Operations
- Manages student records and enrollment
- Stores face embeddings for recognition
- Tracks attendance records
- Manages subject and class information

## Configuration

### Streamlit Config
Configuration files are located in `.streamlit/` directory for customizing the Streamlit application behavior.

## Dependencies

All dependencies are listed in `requirements.txt`. Key packages include:
- streamlit
- scikit-learn
- dlib-bin
- face_recognition_models
- supabase
- librosa
- webrtcvad-wheels

## Usage

1. **Teachers**:
   - Create subjects and classes
   - Upload student photos
   - Monitor attendance
   - View attendance reports
   - Share class QR codes

2. **Students**:
   - Enroll using QR code
   - Upload profile photo
   - Mark attendance via face or voice recognition
   - View personal attendance records

## Troubleshooting

- **Module not found errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Database connection issues**: Check your `.env` file contains valid Supabase credentials
- **Face recognition not working**: Ensure proper lighting and clear face visibility
- **Voice recognition issues**: Check microphone permissions and audio input

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions, please create an issue in the repository.

---

**Note**: Ensure you have the required API keys and database credentials before running the application.
