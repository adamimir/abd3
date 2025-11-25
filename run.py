#!/usr/bin/env python3
"""
Script untuk menjalankan aplikasi Streamlit visualisasi
"""

import os
import sys
import subprocess

def run_streamlit():
    """Jalankan aplikasi Streamlit"""
    
    # Set direktori kerja
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Set environment variables jika belum ada
    if not os.getenv("DB_HOST"):
        os.environ["DB_HOST"] = "localhost"
    if not os.getenv("DB_PORT"):
        os.environ["DB_PORT"] = "5432"
    if not os.getenv("DB_USER"):
        os.environ["DB_USER"] = "postgres"
    if not os.getenv("DB_PASSWORD"):
        os.environ["DB_PASSWORD"] = "12112004"
    if not os.getenv("DB_NAME"):
        os.environ["DB_NAME"] = "visualisasi_abd"
    
    print("=" * 60)
    print("Aplikasi Visualisasi Data Penjualan")
    print("=" * 60)
    print()
    print(f"Direktori: {script_dir}")
    print(f"Host DB: {os.environ['DB_HOST']}")
    print(f"Port DB: {os.environ['DB_PORT']}")
    print(f"User DB: {os.environ['DB_USER']}")
    print(f"Database: {os.environ['DB_NAME']}")
    print()
    print("Meluncurkan Streamlit... buka http://localhost:8501")
    print("Tekan Ctrl+C untuk menghentikan")
    print()
    
    # Jalankan streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    run_streamlit()
