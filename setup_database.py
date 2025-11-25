#!/usr/bin/env python3
"""
Script untuk setup database PostgreSQL untuk aplikasi visualisasi
"""

import psycopg2
import os
import sys

def setup_database():
    """Setup database visualisasi_abd"""
    
    # Konfigurasi koneksi
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", None)
    
    print("=" * 50)
    print("Setup Database Visualisasi ABD")
    print("=" * 50)
    print(f"Host: {DB_HOST}")
    print(f"Port: {DB_PORT}")
    print(f"User: {DB_USER}")
    print()
    
    # Jika password belum diset, minta dari user
    if DB_PASSWORD is None:
        import getpass
        DB_PASSWORD = getpass.getpass("Enter PostgreSQL password: ")
    
    try:
        # Step 1: Koneksi ke PostgreSQL (default postgres database) untuk membuat database
        print("Step 1: Membuat database...")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database="postgres",
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        print("✓ Terhubung ke PostgreSQL")
        
        # Drop dan create database
        cur.execute("DROP DATABASE IF EXISTS visualisasi_abd;")
        cur.execute("CREATE DATABASE visualisasi_abd;")
        print("✓ Database visualisasi_abd berhasil dibuat")
        
        cur.close()
        conn.close()
        
        # Step 2: Koneksi ke database visualisasi_abd untuk membuat table
        print("Step 2: Membuat tabel dan memasukkan data...")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database="visualisasi_abd",
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        print("✓ Terhubung ke database visualisasi_abd")
        
        # Create table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS penjualan (
                id SERIAL PRIMARY KEY,
                bulan VARCHAR(20) NOT NULL,
                produk VARCHAR(50) NOT NULL,
                kategori VARCHAR(30) NOT NULL,
                penjualan INT NOT NULL,
                profit DECIMAL(10, 2) NOT NULL,
                latitude DECIMAL(10, 6),
                longitude DECIMAL(10, 6)
            );
        """)
        print("✓ Tabel penjualan berhasil dibuat")
        
        # Insert data
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
            """INSERT INTO penjualan (bulan, produk, kategori, penjualan, profit, latitude, longitude)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            data
        )
        print("✓ 10 data sample berhasil diinsert")
        
        print("✓ Database dan tabel berhasil dibuat")
        print("✓ 10 data sample berhasil diinsert")
        
        cur.close()
        conn.close()
        
        print()
        print("=" * 50)
        print("Setup Selesai!")
        print("=" * 50)
        print()
        print("Langkah selanjutnya:")
        print("1. Set environment variables:")
        print(f'   $env:DB_HOST = "{DB_HOST}"')
        print(f'   $env:DB_PORT = "{DB_PORT}"')
        print(f'   $env:DB_USER = "{DB_USER}"')
        print(f'   $env:DB_PASSWORD = "{DB_PASSWORD}"')
        print('   $env:DB_NAME = "visualisasi_abd"')
        print()
        print("2. Jalankan aplikasi:")
        print("   streamlit run app.py")
        print()
        
        return True
        
    except psycopg2.Error as e:
        print(f"✗ Error: {e}")
        print()
        print("Pastikan:")
        print("1. PostgreSQL sudah berjalan")
        print("2. Username dan password benar")
        print("3. Host dan port sudah benar")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = setup_database()
    sys.exit(0 if success else 1)
