import psycopg2
from psycopg2.extras import RealDictCursor
import os
import sys

# Try to import streamlit for secrets (in Streamlit Cloud)
try:
    import streamlit as st
    USE_STREAMLIT_SECRETS = True
except ImportError:
    USE_STREAMLIT_SECRETS = False

# Konfigurasi database PostgreSQL (Supabase)
if USE_STREAMLIT_SECRETS and hasattr(st, 'secrets') and 'supabase' in st.secrets:
    # Use Streamlit secrets (for deployment)
    DB_HOST = st.secrets["supabase"]["host"]
    DB_PORT = st.secrets["supabase"]["port"]
    DB_NAME = st.secrets["supabase"]["database"]
    DB_USER = st.secrets["supabase"]["user"]
    DB_PASSWORD = st.secrets["supabase"]["password"]
else:
    # Use environment variables or Supabase defaults (for local development)
    DB_HOST = os.getenv("DB_HOST", "aws-1-ap-south-1.pooler.supabase.com")
    DB_PORT = os.getenv("DB_PORT", "6543")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_USER = os.getenv("DB_USER", "postgres.wtgzrwvxvhoxfeupgmdb")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "AA@12112004@AA")

print(f"[DEBUG] DB Config: {DB_HOST}:{DB_PORT}/{DB_NAME} (User: {DB_USER})", file=sys.stderr)

def get_db_connection():
    """Membuat koneksi ke database PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_all_data():
    """Mengambil semua data penjualan dari database"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM penjualan ORDER BY id")
        data = cur.fetchall()
        cur.close()
        return data
    except psycopg2.Error as e:
        print(f"Error fetching data: {e}")
        return []
    finally:
        conn.close()

def get_sales_by_category():
    """Mengambil data penjualan berdasarkan kategori untuk Pie Chart"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT kategori, SUM(penjualan) as total_penjualan
            FROM penjualan
            GROUP BY kategori
            ORDER BY total_penjualan DESC
        """)
        data = cur.fetchall()
        cur.close()
        return data
    except psycopg2.Error as e:
        print(f"Error fetching category data: {e}")
        return []
    finally:
        conn.close()

def get_sales_by_month():
    """Mengambil data penjualan per bulan untuk Bar/Line Chart"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT bulan, SUM(penjualan) as total_penjualan, SUM(profit) as total_profit,
                   MIN(id) as min_id
            FROM penjualan
            GROUP BY bulan
            ORDER BY min_id
        """)
        data = cur.fetchall()
        cur.close()
        return data
    except psycopg2.Error as e:
        print(f"Error fetching monthly data: {e}")
        return []
    finally:
        conn.close()

def get_locations_data():
    """Mengambil data lokasi untuk Map"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT produk, penjualan, latitude, longitude
            FROM penjualan
            WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        """)
        data = cur.fetchall()
        cur.close()
        return data
    except psycopg2.Error as e:
        print(f"Error fetching location data: {e}")
        return []
    finally:
        conn.close()
