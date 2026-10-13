import streamlit as st
import qrcode
import io
import urllib.parse

# --- KENDİ NUMARANI BURAYA YAZ (Örn: 905321234567) ---
TELEFON_NUMARASI = "905445954532"

st.set_page_config(
    page_title="Şefin Doğum Günü Menüsü",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #b05d49;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .sub-text {
        text-align: center;
        color: #555;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }
    div.stButton > button:first-child {
        background-color: #b05d49;
        color: white;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #964a38;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎉 İyi ki Doğdun Sevgilim</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Bugün mutfak tamamen senin emrinde! Gün boyunca ne yemek ve içmek istersen seç, şefin hazırlasın.</p>", unsafe_allow_html=True)

# Kahvaltı Bölümü
with st.container():
    st.subheader("🍳 Kahvaltı")
    kahvalti_yemek = st.text_input("Kahvaltıda ne yemek istersin?", placeholder="Örn: avacado tost, pankek, tost...")
    kahvalti_icecek = st.text_input("Kahvaltı içeceğin", placeholder="Örn: Portakal suyu, meyve suyu organik full, çay...")

st.write("---")

# Akşam Yemeği Bölümü
with st.container():
    st.subheader("🍷 Akşam Yemeği")
    aksam_yemek = st.text_input("Akşam yemeğinde ne yemek istersin?", placeholder="Örn: ballı hardallı somon, krema mantalı tavuklu makarna ...")
    aksam_icecek = st.text_input("Akşam yemeği içeceğin", placeholder="Örn: Beyaz şarap, kokteyl, kola zero...")

st.write("---")

# Özel İstek Bölümü
with st.container():
    st.subheader("✨ Şefe Özel İstek")
    ozel_not = st.text_area("Tatlı veya gün içine özel bir rica?", placeholder="Örn: Akşam film izlerken sufle de olsun!")

st.write("")

# Gönder Butonu
if st.button("Siparişi Şefe İlet 💌"):
    k_yemek = kahvalti_yemek.strip() or "Şefin seçimi"
    k_icecek = kahvalti_icecek.strip() or "Şefin seçimi"
    a_yemek = aksam_yemek.strip() or "Şefin seçimi"
    a_icecek = aksam_icecek.strip() or "Şefin seçimi"
    not_icerik = ozel_not.strip() or "Yok"

    mesaj = (
        f"🎂 *Doğum Günü Menü Siparişim Geldi!*\n\n"
        f"🍳 *Kahvaltı:*\n- Yemek: {k_yemek}\n- İçecek: {k_icecek}\n\n"
        f"🍷 *Akşam Yemeği:*\n- Yemek: {a_yemek}\n- İçecek: {a_icecek}\n\n"
        f"✨ *Şefe Not:* {not_icerik}"
    )

    encoded_mesaj = urllib.parse.quote(mesaj)
    whatsapp_url = f"https://wa.me/{TELEFON_NUMARASI}?text={encoded_mesaj}"

    st.success("Harika seçimler fıstığımmm Aşağıdaki butona basarak siparişi WhatsApp'tan bana iletebilirsin:")
    st.markdown(
        f'<a href="{whatsapp_url}" target="_blank" style="'
        f'display: block; width: 100%; text-align: center; background-color: #25D366; '
        f'color: white; padding: 14px; border-radius: 10px; text-decoration: none; '
        f'font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">'
        f'WhatsApp ile Siparişi Gönder 💬</a>',
        unsafe_allow_html=True
    )

# Sol Menü (QR Kod Üretici)
with st.sidebar:
    st.header("📲 QR Kod Üretici")
    st.caption("Uygulama linkini buraya yapıştırıp QR kodunu indirebilirsin.")
    
    canli_link = st.text_input("Uygulama Linki", value="https://example.com")
    
    if canli_link:
        qr = qrcode.QRCode(box_size=8, border=2)
        qr.add_data(canli_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#2d2624", back_color="white")
        
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.image(byte_im, caption="Kart İçin QR Kod", use_container_width=True)
        st.download_button(
            label="QR Kodu İndir",
            data=byte_im,
            file_name="menu_qr.png",
            mime="image/png"
        )