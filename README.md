# Gesture Pilot: Gesture Based Interface for Computer Interaction
Gesture Pilot is designed to provide an intuitive and innovative way of interacting with computers. By using hand gestures users can control various aspects of their computer without the need for traditional input devices such as a mouse or keyboard.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Overview](#files-overview)
- [Contributing](#contributing)

## Features

- **Gesture Recognition**: Recognize and interpret various hand gestures to perform different actions.
- **Brightness Control**: Adjust your screen brightness using left-hand gestures.
- **Volume Control**: Manage your system volume with right-hand gestures.
- **Mouse Control**: Use gestures to move your mouse pointer with precision.
- **Streamlit Integration**: A web-based interface to activate and control the gesture recognition features.

## Installation

To get started with the Gesture-Based Interface, clone this repository and install the necessary dependencies.

```bash
git clone https://github.com/AryanMishra1789/Gesture-Based-Interface-for-Computer-Interaction.git
cd Gesture-Based-Interface-for-Computer-Interaction
pip install -r requirements.txt
```

## Usage

Once the installation is complete, you can start the gesture-based interface by running the appropriate scripts.

### Brightness Control
```bash
python brightness_lefthand.py
```

### Volume Control
```bash
python volume_control_righthand.py
```

### Mouse Control
```bash
python mouse_control.py
```

### Streamlit Interface
```bash
streamlit run streamlit.py
```

## Files Overview

- **brightness_lefthand.py**: Script to control screen brightness using left-hand gestures.
- **htm.py**: Contains the `handDetector` class for detecting and tracking hand landmarks.
- **mouse_control.py**: Script to control the mouse pointer using hand gestures.
- **volume_control_righthand.py**: Script to control system volume using right-hand gestures.
- **streamlit.py**: Streamlit-based web interface to activate and control the gesture recognition features.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Thank you for checking out the Gesture-Based Interface for Computer Interaction project. I hope you find it useful and engaging!
