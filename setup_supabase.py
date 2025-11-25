#!/usr/bin/env python3
"""
Script untuk setup database di Supabase PostgreSQL
"""

import psycopg2
import os
import sys
import getpass

def setup_supabase_database():
    """Setup database di Supabase"""
    
    # Supabase Connection String
    # Transaction mode pooler untuk DDL operations
    SUPABASE_URL = "https://wtgzrwvxvhoxfeupgmdb.supabase.co"
    PROJECT_REF = "wtgzrwvxvhoxfeupgmdb"
    
    # Connection details - Transaction pooler
    DB_HOST = "aws-1-ap-south-1.pooler.supabase.com"
    DB_PORT = "6543"  # Pooler port
    DB_NAME = "postgres"
    DB_USER = "postgres.wtgzrwvxvhoxfeupgmdb"
    
    # Minta password dari user
    DB_PASSWORD = os.getenv("SUPABASE_PASSWORD")
    if not DB_PASSWORD:
        print("=" * 70)
        print("Setup Database Supabase - Visualisasi ABD")
        print("=" * 70)
        print(f"Project: {PROJECT_REF}")
        print(f"Host: {DB_HOST}")
        print(f"Database: {DB_NAME}")
        print(f"User: {DB_USER}")
        print()
        DB_PASSWORD = getpass.getpass("Enter Supabase Database Password: ")
    
    try:
        # Koneksi ke Supabase PostgreSQL
        print("\nStep 1: Connecting to Supabase...")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            sslmode='require'  # Supabase requires SSL
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        print("✓ Connected to Supabase PostgreSQL")
        
        # Drop existing table if exists
        print("\nStep 2: Dropping existing table (if any)...")
        cur.execute("DROP TABLE IF EXISTS penjualan CASCADE;")
        print("✓ Old table dropped")
        
        # Create table
        print("\nStep 3: Creating penjualan table...")
        cur.execute("""
            CREATE TABLE penjualan (
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
        print("✓ Table penjualan created")
        
        # Insert sample data
        print("\nStep 4: Inserting sample data...")
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
        print("✓ 10 sample records inserted")
        
        # Verify data
        cur.execute("SELECT COUNT(*) FROM penjualan")
        count = cur.fetchone()[0]
        print(f"✓ Verified: {count} records in database")
        
        cur.close()
        conn.close()
        
        print()
        print("=" * 70)
        print("Setup Complete!")
        print("=" * 70)
        print()
        print("Database is ready on Supabase!")
        print()
        print("Next steps:")
        print("1. Update .streamlit/secrets.toml with your password")
        print("2. Run: streamlit run app.py")
        print()
        print("For Streamlit Cloud deployment:")
        print("Set these secrets in Streamlit Cloud dashboard:")
        print()
        print("[supabase]")
        print(f'host = "{DB_HOST}"')
        print(f'port = "5432"')
        print(f'database = "{DB_NAME}"')
        print(f'user = "{DB_USER}"')
        print(f'password = "YOUR_PASSWORD"')
        print()
        
        return True
        
    except psycopg2.Error as e:
        print(f"\n✗ Database Error: {e}")
        print()
        print("Common issues:")
        print("1. Wrong password - Get it from Supabase Dashboard > Settings > Database")
        print("2. Network/Firewall - Make sure you can access Supabase")
        print("3. SSL required - Connection needs sslmode='require'")
        return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = setup_supabase_database()
    sys.exit(0 if success else 1)
