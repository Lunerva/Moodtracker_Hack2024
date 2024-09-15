from deepface import DeepFace

try:
    analysis = DeepFace.analyze(img_path = "C:/Users/Y700/Desktop/python/HachMTY2024/ANGRY.jpg", actions = ["emotion"])
except:
    print("Windows Error in loading image")

try:
    analysis = DeepFace.analyze(img_path = "ANGRY.jpg", actions = ["emotion"])
except:
    print("Error in loading image")


print(analysis)