import cv2

from tkinter import filedialog

from tkinter import *

cascade_path = "C:\\Users\\petro\\Desktop\\haarcascade_frontalface_default.xml"


def browse_button():
    # Ο χρήστης επιλέγει την εικόνα απο ένα γραφικό μενού Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    face_recognition(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root, textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)


def face_recognition(filename):
    # Δημιουργώ αλληλουχίες απο classifiers τύπου haar.
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Διαβάζει το path της εικόνας και το περνάει σε μία μεταβλητή image
    image = cv2.imread(filename)
    # Μετατρέπει την εικόνα μας, δινοντά της μια γκρι απόχρωση και την περνάει σε μία μεταβλητή grey
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ο αλγόριθμος ανίχνευσης χρησιμοποιεί ένα κινούμενο παράθυρο για την ανίχνευση αντικειμένων.
    # Ο scaleFactor αποτρέπει τα πρόσωπα που είναι πιο κοντά στην κάμερα να φαίνονται μεγαλύτερα
    # To minNeighbors ορίζει πόσα αντικείμενα εντοπίζονται κοντά στo τρέχον πριν δηλώσει το πρόσωπο που βρέθηκε.
    # Το minSize δίνει το μέγεθος του κάθε παραθύρου (μλοκ)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Τυπώνω στην κονσόλα το πόσα πρόσωπα βρέθηκαν
    print("Found {0} faces!".format(len(faces)))

    # Σχεδιάζω ένα ορθογώνιο γύρω απο το πρόσωπο.
    # Tα x και y είναι οι πλευρές του rectangle και τα w και h είναι width και high αντίστοιχα
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Εμφανίζω την εικόνα με κυκλομένα τα πρόσωπα
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)


mainloop()
