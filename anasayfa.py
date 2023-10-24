import tkinter as tk
from PIL import Image, ImageTk

# # Ana pencere oluşturma
# root = tk.Tk()
# root.title("Online Kurs Yönetim Sistemi")

def make_widgets(root):
    root.title("Anasayfa")
    # Resimleri yükle
    my_courses_image = Image.open("kurslarım.jpg").resize((310, 310))
    my_courses_photo = ImageTk.PhotoImage(my_courses_image)

    other_courses_image = Image.open("diger_kurslar.jpg").resize((310, 310))
    other_courses_photo = ImageTk.PhotoImage(other_courses_image)

    profile_image = Image.open("profile.jpg").resize((310, 310))
    profile_photo = ImageTk.PhotoImage(profile_image)

    statistics_image = Image.open("istatistik.jpg").resize((310, 310))
    statistics_photo = ImageTk.PhotoImage(statistics_image)

    # Başlık etiketi
    title_label = tk.Label(root, text="Online Kurs Yönetim Sistemi", font=("Arial", 24))
    title_label.grid(row=0, column=0, columnspan=4, pady=20)

    # Butonlar
    my_courses_button = tk.Button(root, image=my_courses_photo, command=button_click)
    my_courses_button.grid(row=1, column=0, padx=10, pady=10)
    my_courses_button.image = my_courses_photo

    my_courses_label = tk.Label(root, text="Kurslarım", font=("Arial", 20))
    my_courses_label.grid(row=2, column=0, padx=10, pady=10)

    other_courses_button = tk.Button(root, image=other_courses_photo, command=button_click)
    other_courses_button.grid(row=1, column=1, padx=10, pady=10)
    other_courses_button.image = other_courses_photo

    other_courses_label = tk.Label(root, text="Diğer Kurslar", font=("Arial", 20))
    other_courses_label.grid(row=2, column=1, padx=10, pady=10)

    profile_button = tk.Button(root, image=profile_photo, command=button_click)
    profile_button.grid(row=1, column=2, padx=10, pady=10)
    profile_button.image = profile_photo

    profile_label = tk.Label(root, text="Profilim", font=("Arial", 20))
    profile_label.grid(row=2, column=2, padx=10, pady=10)

    istatistik_button = tk.Button(root, image=statistics_photo, command=button_click())
    istatistik_button.grid(row=1, column=3, padx=10, pady=10)
    istatistik_button.image = statistics_photo

    istatistik_label = tk.Label(root, text="İstatistikler", font=("Arial", 20))
    istatistik_label.grid(row=2, column=3, padx=10, pady=10)

    # Label for button click event
    label = tk.Label(root, text="", font=("Arial", 12))
    label.grid(row=2, column=0, columnspan=4, pady=10)

# Fonksiyon: Butona tıklandığında yapılacak işlem
def button_click():
    print("buton click edildi")

# make_widgets(root)

# Pencereyi çalıştır
# root.mainloop()