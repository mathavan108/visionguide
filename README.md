# AI-Powered Wearable Assistant for Visually Impaired Users

## Team Details
| Name | Role |
|------|------|
| Mathavan P | Camera Module |
| Surya P| Vision Language Model |
| Vignesh M | Navigation Guidance |
| Vijay ragavan| Speech Module |
| Shreyas S| System Integration |
| Rathish B| Speech and audio |

## Problem Statementgit add README.md

## Features 

Captures the user's surroundings in real time using a camera.
Analyzes the environment using a Vision-Language AI model.
Detects and identifies objects, people, pathways, and obstacles.
Provides intelligent voice guidance for safe and independent navigation.
Generates simple and easy-to-understand navigation instructions.
Delivers real-time audio feedback with minimal delay.
Supports hands-free operation through headphones.
Portable and lightweight prototype suitable for everyday use.
Designed with accessibility and ease of use as the primary focus.
Operates locally on the prototype device without requiring continuous internet access.
Modular architecture that can be deployed on edge devices such as Raspberry Pi in future versions.
Enhances user confidence and independence while navigating unfamiliar environments.

## System Architecture

Wearable Camera
       │
       ▼
 Image Capture
       │
       ▼
Vision-Language AI Model
       │
       ▼
 Scene Understanding
       │
       ▼
Navigation Decision Engine
       │
       ▼
Text-to-Speech
       │
       ▼
Headphones / Speaker
       │
       ▼
User Receives Voice Guidance

## Tech stack


Programming Language

 Python

 Computer Vision

 OpenCV

 Artificial Intelligence

 Vision-Language Model (VLM)
 Hugging Face Transformers

 Image Processing

 Pillow (PIL)

 Speech Processing

 Text-to-Speech (TTS)

 Development Tools

Visual Studio Code
 Git
GitHub

 Hardware

 Laptop (Prototype)
 Webcam / Wearable Camera
 Headphones

Operating System

Windows / macOS / Linux

## Folder Structure

Folder Structure

VisionGuide-AI/

│

├── assets/                 

├── dataset/                

├── models/                 

├── src/                    
│   ├── camera.py           

│   ├── ai_model.py         
│   ├── navigation.py      

│   ├── speech.py           
│   └── main.py             

│

├── requirements.txt        

├── README.md               

└── LICENSE                 

## Installation

1. Clone the Repository
git clone https://github.com/mathavan108/visionguide
cd VisionGuide-AI
2. Create a Virtual Environment (Optional)
python -m venv venv
3. Activate the Virtual Environment

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate
4. Install Required Packages
pip install -r requirements.txt
5. Connect the Camera

Connect a webcam or wearable camera and ensure it is detected by your system.

6. Run the Project
python src/main.py
## Workflow

Camera
   │
   ▼
Capture Live Image
   │
   ▼
Image Preprocessing
   │
   ▼
Vision-Language AI Model
   │
   ▼
Scene Understanding
   │
   ▼
Object & Hazard Detection
   │
   ▼
Navigation Decision
   │
   ▼
Text-to-Speech
   │
   ▼
Voice Guidance
   │
   ▼
User

## Usage

Launch the application.
Position the camera toward the surrounding environment.
The system continuously captures live images.
The AI analyzes the scene and identifies important objects and obstacles.
Navigation instructions are generated based on the detected environment.
The instructions are converted into speech.
Listen to the voice guidance through headphones and navigate safely.


## AI Workflow

The camera captures the user's surroundings in real time.
The captured image is sent to the Vision-Language AI model.
The AI analyzes the scene and identifies important objects, people, pathways, and potential hazards.
The system generates simple and meaningful navigation instructions.
The instructions are converted into speech using a Text-to-Speech engine.
The user receives real-time voice guidance through headphones for safe navigation.

## Hardware Components

Laptop (Prototype)
Webcam or Wearable Camera
Headphones
USB Cable / Power Supply


## Security Measures

Processes images locally during the prototype to protect user privacy.
Does not permanently store captured images or personal data.
Minimizes unnecessary data collection.
Designed with user safety and privacy in mind.

## Testing

Live camera capture.
AI-based scene understanding.
Object and obstacle detection.
Voice guidance generation.
End-to-end system integration.
## Performance

The system provides real-time scene analysis and voice guidance with minimal delay. It successfully identifies common objects and obstacles, helping users navigate more safely. Performance may vary depending on lighting conditions and hardware capabilities.

## Challenges

Running AI models efficiently on limited hardware.
Maintaining real-time response speed.
Handling poor lighting and crowded environments.
Integrating multiple modules within a short hackathon timeline.
Ensuring accurate and meaningful voice guidance.

## Future Scope

Deploy the system on Raspberry Pi or other edge devices.
Add GPS support for outdoor navigation.
Integrate OCR to read signboards and room numbers.
Estimate the distance to nearby objects.
Support multilingual voice guidance.
Add voice command functionality.
Improve AI accuracy in complex environments.

## Demo

The demonstration showcases the complete workflow of the system:

Capture the user's surroundings.
Analyze the scene using the AI model.
Detect important objects and hazards.

## Advanced Personalization Module

### Purpose

The Advanced Personalization Module adds a lifelong user-centric navigation layer to the project. It is designed to adapt guidance recommendations based on individual profile settings and scene context.

### Motivation

The main system delivers general assistance, but people with different mobility patterns and navigation preferences benefit from personalized support. This module makes navigation instructions feel more natural, consistent, and aligned with each user's preferred direction and behavior.

### Features

- Persistent user profile management
- Preference-aware direction guidance
- Scene object recognition for adaptive recommendations
- Rule-based environment awareness
- History tracking for obstacles and locations

### Workflow

1. Load or initialize the user profile.
2. Interpret the current scene description.
3. Detect supported objects and environment type.
4. Generate guidance based on user preferences and scene context.
5. Update the profile with new obstacles and location data.
6. Persist the updated profile for future sessions.

### Folder location

The module is implemented under:

- `advanced_features/`

### Integration with the main project

The module is designed to complement the existing navigation engine. It can be integrated by feeding scene descriptions into the personalization guidance pipeline and then combining its output with the primary navigation decisions and speech system.

### Future scope

- Extend user profile schemas with richer preference data
- Add feedback-driven adaptation over time
- Integrate multi-modal signals such as voice and environment sensors
- Improve rule-based guidance with more scene-aware behaviors
- Support cross-session personalization analytics

Generate navigation instructions.
Convert the instructions into speech.
Provide real-time voice guidance to the user.

## References

Python Documentation
OpenCV Documentation
Hugging Face Transformers Documentation
Vision-Language Model Documentation (SmolVLM / Moondream)
Research papers on AI-based assistive technologies for visually impaired individuals

## License

This project was developed as part of a 24-hour hackathon for educational and research purposes. It demonstrates the use of Artificial Intelligence and Computer Vision to improve accessibility for visually impaired individuals.

This project may be used, modified, and extended for learning, research, and non-commercial purposes with appropriate credit to the development team.