import sqlite3
import pandas as pd

def init_sqlite_db():
    """Initialize SQLite database for deployment"""
    conn = sqlite3.connect('visualisasi.db')
    cur = conn.cursor()
    
    # Create table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS penjualan (
            id INTEGER PRIMARY KEY,
            bulan TEXT,
            produk TEXT,
            kategori TEXT,
            penjualan INTEGER,
            profit REAL,
            latitude REAL,
            longitude REAL
        )
    ''')
    
    # Insert sample data
    data = [
        ('Januari', 'Laptop', 'Elektronik', 15, 4500000, -6.2088, 106.8456),
        ('Februari', 'Mouse', 'Elektronik', 45, 1350000, -6.1751, 106.8650),
        ('Maret', 'Keyboard', 'Elektronik', 30, 1200000, -6.1944, 106.8296),
        ('April', 'Monitor', 'Elektronik', 20, 3000000, -6.1753, 106.9270),
        ('Mei', 'Headset', 'Elektronik', 50, 2000000, -6.2298, 106.7852),
        ('Juni', 'Webcam', 'Elektronik', 35, 1050000, -6.1447, 106.8256),
        ('Juli', 'SSD', 'Penyimpanan', 25, 3000000, -6.1751, 106.8650),
        ('Agustus', 'RAM', 'Penyimpanan', 40, 2000000, -6.2088, 106.8456),
        ('September', 'Router', 'Jaringan', 18, 1800000, -6.1944, 106.8296),
        ('Oktober', 'Printer', 'Perangkat', 22, 2200000, -6.1753, 106.9270)
    ]
    
    cur.executemany(
        'INSERT OR REPLACE INTO penjualan (bulan, produk, kategori, penjualan, profit, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)',
        data
    )
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_sqlite_db()
    print("SQLite database created successfully!")
