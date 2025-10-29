import cv2
 
image_path = 'c:\\Users\\dimal.DIMON-2024\\Desktop\\Theproject234\\Theproject234'
cascade_path = 'c:\\Users\\dimal.DIMON-2024\\Desktop\\Theproject234\\Theproject234'
 
image = cv2.imread(image_path)
if image is None:
    print("ПОМИЛКА: Зображення не завантажено! Перевірте шлях до файлу.")
else:
    print(f"Зображення завантажено. Розмір: {image.shape}")
 
cat_face_cascade = cv2.CascadeClassifier(cascade_path)
if cat_face_cascade.empty():
    print("ПОМИЛКА: XML-файл каскаду не завантажено! Перевірте шлях.")
else:
    print("Каскад завантажено успішно")
 
cat_face = cat_face_cascade.detectMultiScale(image)
 
print(f"Знайдено мордочок котів: {len(cat_face)}")
print(f"Координати: {cat_face}")
 
cv2.imshow("Cat", image)
cv2.waitKey()
cv2.destroyAllWindows()
 