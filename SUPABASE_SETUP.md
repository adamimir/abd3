# 🚀 Setup Supabase Database

## Langkah-langkah:

### 1. Dapatkan Password Database dari Supabase

1. Buka Supabase Dashboard: https://supabase.com/dashboard
2. Pilih project: **wtgzrwvxvhoxfeupgmdb**
3. Klik **Settings** (icon gear) di sidebar
4. Klik **Database**
5. Scroll ke **Connection string** atau **Database password**
6. Copy password database Anda

### 2. Setup Database

Jalankan script setup:

```powershell
python setup_supabase.py
```

Masukkan password saat diminta.

### 3. Update Secrets (Untuk Local Development)

Edit file `.streamlit/secrets.toml` dan ganti `YOUR_SUPABASE_PASSWORD_HERE` dengan password Anda.

### 4. Jalankan Aplikasi

```powershell
streamlit run app.py
```

---

## 📋 Untuk Deploy ke Streamlit Cloud

1. Push code ke GitHub
2. Buka Streamlit Cloud: https://share.streamlit.io
3. Deploy app dari repo GitHub
4. Klik **Settings** → **Secrets**
5. Paste konfigurasi berikut (ganti password):

```toml
[supabase]
host = "db.wtgzrwvxvhoxfeupgmdb.supabase.co"
port = "5432"
database = "postgres"
user = "postgres.wtgzrwvxvhoxfeupgmdb"
password = "YOUR_SUPABASE_PASSWORD"
```

6. Save dan app akan auto-restart
7. ✅ Done! App sudah online

---

## 🔧 Troubleshooting

**Error: password authentication failed**
- Pastikan password benar dari Supabase Dashboard → Settings → Database

**Error: SSL connection failed**
- Supabase memerlukan SSL, pastikan `sslmode='require'` di connection

**Error: could not connect to server**
- Check internet connection
- Pastikan firewall tidak block koneksi ke Supabase

---

## ✅ Connection Details

- **Host**: db.wtgzrwvxvhoxfeupgmdb.supabase.co
- **Port**: 5432
- **Database**: postgres
- **User**: postgres.wtgzrwvxvhoxfeupgmdb
- **SSL Mode**: require

---

**Supabase Project URL**: https://wtgzrwvxvhoxfeupgmdb.supabase.co
