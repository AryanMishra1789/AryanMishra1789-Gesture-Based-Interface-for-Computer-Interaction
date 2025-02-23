# Gesture Pilot: Gesture-Based Interface for Computer Interaction
Welcome to Gesture Pilot! This project aims to revolutionize the way you interact with your computer using intuitive hand gestures. Dive in to explore a new dimension of user interaction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Brightness Control](#brightness-control)
  - [Volume Control](#volume-control)
  - [Mouse Control](#mouse-control)
  - [Streamlit Interface](#streamlit-interface)
- [Files Overview](#files-overview)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Gesture Pilot is designed to provide an intuitive and innovative way of interacting with computers. By using gesture recognition, users can control various aspects of their computer without the need for traditional input devices such as a mouse or keyboard.

## Features
- **Gesture Recognition**: Recognize and interpret various hand gestures to perform different actions.
- **Brightness Control**: Adjust your screen brightness using left-hand gestures.
- **Volume Control**: Manage your system volume with right-hand gestures.
- **Mouse Control**: Use gestures to move your mouse pointer with precision.
- **Streamlit Integration**: A web-based interface to activate and control the gesture recognition features.

## Installation
To get started with Gesture Pilot, follow these steps:

1. **Install Python 3.10**: Download and install Python 3.10 from the [official website](https://www.python.org/downloads/release/python-3100/).

2. **Clone the repository**:
   ```bash
   git clone https://github.com/AryanMishra1789/Gesture-Based-Interface-for-Computer-Interaction.git
   cd Gesture-Based-Interface-for-Computer-Interaction
   ```

3. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the necessary dependencies**:
   ```bash
   pip install --upgrade pip setuptools
   pip install -r requirements.txt
   ```

## Usage
Once the installation is complete, follow these steps to use Gesture Pilot:.

### Streamlit Interface
Launch the Streamlit web interface to interact with Gesture Pilot via a user-friendly UI.
```bash
streamlit run streamlit.py
```
### Brightness Control
**Gesture to use:** Move your Index Finger and Thumb of the Left Hand to increase or decrease brightness.

### Volume Control
**Gesture to use:** Move your Index Finger and Thumb of the Right Hand to increase or decrease volume.

### Mouse Control
**Gesture to use:** Move your Index Finger of any hand to control the mouse pointer movement.

## Files Overview
- `brightness_lefthand.py`: Script to control screen brightness using left-hand gestures.
- `htm.py`: Contains the handDetector class for detecting and tracking hand landmarks.
- `mouse_control.py`: Script to control the mouse pointer using hand gestures.
- `volume_control_righthand.py`: Script to control system volume using right-hand gestures.
- `streamlit.py`: Streamlit-based web interface to activate and control the gesture recognition features.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Thank you for checking out the Gesture Pilot project. I hope you find it useful and engaging!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
