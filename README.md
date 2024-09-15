![](https://drive.google.com/file/d/1BkGc1_trCGbch64M3h9EEO99xhvdBqAG/view?usp=drive_link)
# Moodtracker

Moodtracker aims to improve working conditions, diagnosing and subsequently recommending a certain treatment to relieve stress or any abnormal condition
in the worker, this through technologies such as OpenVINO and Frida, the program. The program will subsequently send feedback to the employer or manager and he or she will take the respective measures.

## Tools taking part of the project
### Install deepface form Git

```rub
#Repo: https://github.com/serengil/deepface
pip install deepface
```

```rub
from deepface import DeepFace
analysis = DeepFace.analyze(img_path = "img.jpg", actions = ["emotion"])
print(analysis)
```
### Install OpenVINO using a virtual environment

Create a virtual environment
```rub
python -m venv openvino_env
```
Get into the virtual environment
```rub
openvino_env\Scripts\activate
```
Get sure python is on latest version
```rub
python -m pip install --upgrade pip
```
Install OpenVino
```rub
pip install openvino==2024.3.0
```

## Contribution

Moodtracler contributes enhancing human life quality through all industries, making sure the most valuable part of the organization or institution, human part, is performing with the best conditions avaiable, simultaneously making them work in a more efficient way.



