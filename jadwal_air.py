import streamlit as st
from datetime import datetime
import pytz
import streamlit.components.v1 as components

# Konfigurasi halaman
st.set_page_config(page_title="💧 Jadwal Minum Air", layout="centered")

# Tambahkan CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #cceeff, #e6f7ff);
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #cdeefd, #f0fcff);
}
.card {
    background: rgba(255, 255, 255, 0.85);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Fungsi notifikasi browser
def show_browser_notification(title, message):
    components.html(f"""
        <script>
        Notification.requestPermission().then(function(permission) {{
            if (permission === "granted") {{
                new Notification("{title}", {{
                    body: "{message}",
                    icon: "https://cdn-icons-png.flaticon.com/512/728/728093.png"
                }});
            }}
        }});
        </script>
    """, height=0)

# Judul
st.markdown("<h1 style='text-align: center; color: #00BFFF;'>💧 Jadwal Minum Air Putih</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Target: 8 Gelas (Total 2 Liter per Hari)</p>", unsafe_allow_html=True)

# Jadwal + volume per gelas (ml)
schedule = [
    ("08:00", "Setelah bangun tidur", 250),
    ("10:00", "Pagi", 250),
    ("12:00", "Sebelum makan siang", 250),
    ("14:00", "Setelah makan siang", 250),
    ("16:00", "Sore", 250),
    ("17:30", "Setelah aktivitas sore", 250),
    ("19:00", "Sebelum makan malam", 250),
    ("21:00", "Sebelum tidur", 250)
]

# Waktu sekarang
tz = pytz.timezone('Asia/Jakarta')
now = datetime.now(tz).strftime("%H:%M")
drunk_count = 0
drunk_ml = 0

# Jadwal tampilan
st.markdown("---")
st.subheader("📅 Jadwal Hari Ini:")

for time_str, note, volume in schedule:
    if now >= time_str:
        status = "✅ Sudah Lewat"
        drunk_count += 1
        drunk_ml += volume
        color = "#e2f7e1"
    else:
        status = "⏰ Akan Datang"
        color = "#eef8fd"

    st.markdown(
        f"""
        <div class='card' style="background-color:{color};">
            <strong>🕗 {time_str}</strong> - {note}<br>
            <small>{status} • {volume} ml</small>
        </div>
        """, unsafe_allow_html=True
    )

# Progress
st.markdown("---")
st.subheader("🚰 Progress Minum Air Hari Ini:")
st.progress(drunk_count / 8.0)
st.write(f"Sudah minum **{drunk_count} dari 8 gelas** (**{drunk_ml} ml** dari 2000 ml).")

# Notifikasi web
for time_str, note, volume in schedule:
    if now == time_str:
        show_browser_notification(
            "⏰ Saatnya Minum Air!",
            f"{note} (Jam {time_str}) - Minumlah {volume} ml 💧"
        )

# Tips
st.markdown("---")
st.success("💡 Tips: Minum air cukup bantu tubuh tetap segar, sehat, dan fokus sepanjang hari!")

# Gambar
st.image("https://cdn-icons-png.flaticon.com/512/728/728093.png", width=100, caption="Tetap terhidrasi ya!")

# Hak cipta
st.markdown("""
<hr style="margin-top: 30px;"/>
<p style='text-align: center; font-size: 14px; color: gray;'>
    © 2025 Aliyyah Syafiqah Lubis.
</p>
""", unsafe_allow_html=True)
