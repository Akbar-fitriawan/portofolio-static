# from app import create_app
# from app.extensions import db
# from app.auth.models import User
# from werkzeug.security import generate_password_hash, check_password_hash


# app = create_app()
# with app.app_context():
#     # Buat pengguna baru
#     # new_user = User(username='Akbar_fitriawan0012', email='akbarfitriawan12@gmail.com')
#     # new_user.set_password('Afitriawan0012')  # Menggunakan metode untuk hash password
#     new_user = User(username='Akbar_fitriawan0012', email='akbarfitriawan12@gmail.com', password=generate_password_hash('Afitriawan0012'))

#     # Tambahkan pengguna ke database dan simpan
#     db.session.add(new_user)
#     db.session.commit()

#     print("User created successfully.")
