import streamlit as st
import random
import speech_recognition as sr
import time

# Fungsi untuk menghasilkan soal matematika
def generate_question(level):
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} + {b}"
        answer = a + b
    elif level == 2:
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} - {b}"
        answer = a - b
    elif level == 3:
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} * {b}"
        answer = a * b
    elif level == 4:
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"{a} / {b}"
        answer = a / b
    else:
        a, b = random.randint(1, 20), random.randint(1, 20)
        question = f"{a} + {b} * {random.randint(1, 5)}"
        answer = a + b * random.randint(1, 5)
    
    return question, answer

# Fungsi untuk mendeteksi suara
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Silakan ucapkan jawaban Anda...")
        audio = r.listen(source)
        try:
            answer = r.recognize_google(audio)
            st.write(f"Jawaban yang terdeteksi: {answer}")
            return answer
        except sr.UnknownValueError:
            st.write("Maaf, tidak dapat mendeteksi suara.")
            return None
        except sr.RequestError:
            st.write("Tidak dapat menghubungi layanan pengenalan suara.")
            return None

# Streamlit UI
st.title("Math Speak Challenge")
st.write("Selamat datang di Math Speak Challenge! Ucapkan jawaban Anda.")

# Inisialisasi variabel
level = 1
score = 0
questions_answered = 0

while True:
    # Menghasilkan soal
    question, answer = generate_question(level)
    st.write(f"Soal: {question}")

    # Menentukan waktu berdasarkan level
    if level <= 2:
        timer = 10
    elif level <= 4:
        timer = 8
    else:
        timer = 6

    # Timer
    start_time = time.time()
    user_answer = recognize_speech()
    elapsed_time = time.time() - start_time

    # Cek jawaban
    if user_answer is not None:
        questions_answered += 1
        if elapsed_time < timer:
            if float(user_answer) == answer:
                st.success("✅ Benar!")
                score += 1
                level += 1
            else:
                st.error("❌ Salah!")
        else:
            st.error("❌ Waktu habis!")

    # Tampilkan skor dan statistik
    st.write(f"Skor: {score}")
    st.write(f"Jumlah soal dijawab: {questions_answered}")
    st.write(f"Level saat ini: {level}")

    # Opsi untuk melanjutkan atau keluar
    if st.button("Lanjutkan"):
        continue
    else:
        break

st.write("Terima kasih telah bermain!")
