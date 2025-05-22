import streamlit as st
from datetime import datetime

# --- KONFIGURASI STREAMLIT ---
st.set_page_config(page_title="𝑳𝒂 𝑽𝒊𝒆 𝒆𝒏 𝑭𝒍𝒆𝒖𝒓𝒔", page_icon="🌷")
st.sidebar.title("𝑴𝒆𝒏𝒖")
halaman = st.sidebar.radio("𝐏𝐢𝐥𝐢𝐡 𝐡𝐚𝐥𝐚𝐦𝐚𝐧:", ["𝐏𝐫𝐨𝐟𝐢𝐥 𝐓𝐨𝐤𝐨", "𝐏𝐫𝐨𝐟𝐢𝐥 𝐏𝐞𝐦𝐞𝐬𝐚𝐧", "𝐏𝐞𝐦𝐞𝐬𝐚𝐧𝐚𝐧", "𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐬𝐚𝐧𝐚𝐧", "𝐏𝐞𝐦𝐛𝐚𝐲𝐚𝐫𝐚𝐧"])

# --- DATA HARGA ---
harga_bouquet = {
    "A": 50000, 
    "B": 35000, 
    "C": 20000}
harga_size = {
    "A": 0, 
    "B": 10000, 
    "C": 20000}
harga_aksesoris = {
    "A": 5000, 
    "B": 2000, 
    "C": 15000, 
    "D": 10000, 
    "E": 5000}

# --- HALAMAN PROFIL TOKO ---
if halaman == "𝐏𝐫𝐨𝐟𝐢𝐥 𝐓𝐨𝐤𝐨":
    st.title("🌷 𝑳𝒂 𝑽𝒊𝒆 𝒆𝒏 𝑭𝒍𝒆𝒖𝒓𝒔")
    st.caption("𝒀𝒐𝒖𝒓 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍𝒊𝒛𝒆𝒅 𝒃𝒐𝒖𝒒𝒖𝒆𝒕, 𝒃𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍𝒍𝒚 𝒂𝒓𝒓𝒂𝒏𝒈𝒆𝒅")
    st.image(
        "bouquetpp.jpg",
        caption="Celebrate Every Moment with La Vie en Fleurs 💐",
        use_container_width=True
    )
    st.markdown("""
    ## 𝑻𝒆𝒏𝒕𝒂𝒏𝒈 𝑲𝒂𝒎𝒊
    **La Vie en Fleurs** adalah toko buket bunga yang mengutamakan personalisasi dan keindahan dalam setiap rangkaian.

    Kami menyediakan berbagai pilihan bunga segar, buatan, dan kreatif seperti pipe cleaner, serta aneka aksesoris untuk mempercantik buketmu.

    - Alamat: Jl. Mawar Indah No. 5, Bandung  
    - WhatsApp: [**0857-XXXX-XXXX**] 
    - Instagram: [@shimaratu4](https://instagram.com/shimaratu4)  
    """)
    st.image(
        "bouquetlast.jpg",
        caption="🌸Choose your dream Bouquet !",
        use_container_width=True
    )

# --- HALAMAN PROFIL PEMESAN ---
elif halaman == "𝐏𝐫𝐨𝐟𝐢𝐥 𝐏𝐞𝐦𝐞𝐬𝐚𝐧":
    st.title("👤 𝑷𝒓𝒐𝒇𝒊𝒍 𝑷𝒆𝒎𝒆𝒔𝒂𝒏")
    nama = st.text_input("Nama Lengkap")
    kontak = st.text_input("Nomor WhatsApp")
    alamat = st.text_area("Alamat Pengiriman")
    if nama and kontak and alamat:
        st.session_state['profil'] = {
            "nama": nama,
            "kontak": kontak,
            "alamat": alamat
        }
    if st.button("✅ Simpan Data"):
        st.success("Data profil di simpan.")

# --- HALAMAN PEMESANAN ---
elif halaman == "𝐏𝐞𝐦𝐞𝐬𝐚𝐧𝐚𝐧":
    st.title("🌷 𝑳𝒂 𝑽𝒊𝒆 𝒆𝒏 𝑭𝒍𝒆𝒖𝒓𝒔")
    st.caption("𝒀𝒐𝒖𝒓 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍𝒊𝒛𝒆𝒅 𝒃𝒐𝒖𝒒𝒖𝒆𝒕, 𝒃𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍𝒍𝒚 𝒂𝒓𝒓𝒂𝒏𝒈𝒆𝒅")

    st.header("1. 𝑷𝒊𝒍𝒊𝒉 𝑱𝒆𝒏𝒊𝒔 𝑩𝒐𝒖𝒒𝒖𝒆𝒕")
    jenis_opsi = {
        "A. Fresh Flower 💐 - Rp50.000": "A",
        "B. Artificial 🌼 - Rp35.000": "B",
        "C. Pipe Cleaner 🌸 - Rp20.000": "C"
    }

    jenis_input = st.selectbox("Pilih jenis bouquet:", list(jenis_opsi.keys()))
    kode_jenis = jenis_opsi[jenis_input]
    harga_jenis = harga_bouquet[kode_jenis]

    # --- GAMBAR JENIS BOUQUET ---
    st.image(
    "bouquetjenis.jpg.jpeg",
    caption="CHOOSE UR OWN BOUQUET 💐",
    use_container_width=True
    )

    st.header("2. 𝑷𝒊𝒍𝒊𝒉 𝑼𝒌𝒖𝒓𝒂𝒏")
    ukuran_opsi = {
        "A. Small - Rp0": "A",
        "B. Medium - Rp10.000": "B",
        "C. Large - Rp20.000": "C"
    }
    ukuran_input = st.radio("Ukuran bouquet:", list(ukuran_opsi.keys()))
    kode_ukuran = ukuran_opsi[ukuran_input]
    harga_ukuran = harga_size[kode_ukuran]

    st.header("3. 𝑻𝒂𝒎𝒃𝒂𝒉 𝑨𝒌𝒔𝒆𝒔𝒐𝒓𝒊𝒔")
    st.warning("📌 *Note: Mohon maaf kami tidak menerima request khusus. Semua produk yang ready hanya tertera di katalog kami.*")
    aks_opsi = {
        "A. Pita 🎀 - Rp5.000": "A",
        "B. Kartu Ucapan 📝 - Rp2.000": "B",
        "C. Boneka 🧸 - Rp15.000": "C",
        "D. Lampu LED ✨ - Rp10.000": "D",
        "E. Kupu-kupu 🦋 - Rp5.000": "E"
    }
    aks_input = st.multiselect("Pilih aksesoris:", list(aks_opsi.keys()))
    kode_aks = [aks_opsi[a] for a in aks_input]
    harga_aks_total = sum([harga_aksesoris[k] for k in kode_aks])

    total_semua = harga_jenis + harga_ukuran + harga_aks_total

    st.session_state['pesanan'] = {
        "kode_jenis": kode_jenis,
        "jenis_input": jenis_input,
        "harga_jenis": harga_jenis,
        "kode_ukuran": kode_ukuran,
        "ukuran_input": ukuran_input,
        "harga_ukuran": harga_ukuran,
        "kode_aks": kode_aks,
        "harga_aks_total": harga_aks_total,
        "total_semua": total_semua
    }

# --- HALAMAN RINGKASAN TOTAL ---
elif halaman == "𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐬𝐚𝐧𝐚𝐧":
    st.title("🧾 𝑹𝒊𝒏𝒈𝒌𝒂𝒔𝒂𝒏 𝑷𝒆𝒔𝒂𝒏𝒂𝒏 𝑨𝒏𝒅𝒂")
    pesanan = st.session_state.get('pesanan', {})

    if pesanan:
        with st.expander("📦 Lihat Detail"):
            st.write(f"- **Jenis bouquet:** {pesanan['kode_jenis']} ({pesanan['jenis_input']}) → Rp{pesanan['harga_jenis']}")
            st.write(f"- **Ukuran bouquet:** {pesanan['kode_ukuran']} ({pesanan['ukuran_input']}) → Rp{pesanan['harga_ukuran']}")
            if pesanan['kode_aks']:
                st.write(f"- **Aksesoris:** {', '.join(pesanan['kode_aks'])} → Rp{pesanan['harga_aks_total']}")
            else:
                st.write("- **Aksesoris:** Tidak ada")
            st.markdown(f"### 💰 Total Pesanan: Rp{pesanan['total_semua']}")
    else:
        st.warning("Belum ada pesanan.")

# --- HALAMAN PEMBAYARAN ---
elif halaman == "𝐏𝐞𝐦𝐛𝐚𝐲𝐚𝐫𝐚𝐧":
    st.title("💳 𝑴𝒆𝒕𝒐𝒅𝒆 𝑷𝒆𝒎𝒃𝒂𝒚𝒂𝒓𝒂𝒏")

    metode = st.radio("Pilih metode pembayaran:", ["Tunai", "QRIS"])
    if metode == "Tunai":
        st.info("Silakan bayar langsung di tempat.")
    else:
        st.image("qris.jpg.jpeg", use_container_width=True)
        st.info("Silakan scan QR code untuk menyelesaikan pembayaran (SHOPEEEPAY ONLY ).")

    if st.button("✅ Konfirmasi Pembayaran"):
        st.success("Pembayaran dikonfirmasi.")

        # Tampilkan struk
        profil = st.session_state.get('profil', {})
        pesanan = st.session_state.get('pesanan', {})
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.markdown("---")
        st.subheader("🧾 𝑺𝒕𝒓𝒖𝒌 𝑷𝒆𝒎𝒃𝒂𝒚𝒂𝒓𝒂𝒏")
        st.text(f"Waktu        : {waktu}")
        st.text(f"Nama Pemesan : {profil.get('nama', '-')}")
        st.text(f"No. WhatsApp : {profil.get('kontak', '-')}")
        st.text(f"Alamat       : {profil.get('alamat', '-')}")
        st.text(" ")
        st.text(f"Jenis        : {pesanan.get('jenis_input', '-')}")
        st.text(f"Ukuran       : {pesanan.get('ukuran_input', '-')}")
        aks = ", ".join(pesanan.get("kode_aks", [])) if pesanan.get("kode_aks") else "Tidak ada"
        st.text(f"Aksesoris    : {aks}")
        st.text(f"Total Bayar  : Rp{pesanan.get('total_semua', 0)}")
        st.text(f"Metode Bayar : {metode}")

    st.markdown("---")
    st.header("📞 Contact Person")
    st.info("""
    📱 WhatsApp: **0857-XXXX-XXXX** (Shima Ratu Donita)  
    📷 Instagram: **[@shimaratu4](https://instagram.com/shimaratu4)**  
    💬 Untuk pertanyaan, pesanan khusus, dan konfirmasi pembayaran.
    """)
