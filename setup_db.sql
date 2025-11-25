-- Buat database visualisasi
DROP DATABASE IF EXISTS visualisasi_abd;
CREATE DATABASE visualisasi_abd;

-- Koneksi ke database visualisasi_abd dilakukan di aplikasi Python
-- Buat table penjualan dengan 10 data sample
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

-- Insert 10 data sample
INSERT INTO penjualan (bulan, produk, kategori, penjualan, profit, latitude, longitude) VALUES
('Januari', 'Laptop', 'Elektronik', 15, 4500000, -6.2088, 106.8456),
('Februari', 'Mouse', 'Elektronik', 45, 1350000, -6.1751, 106.8650),
('Maret', 'Keyboard', 'Elektronik', 30, 1200000, -6.1944, 106.8296),
('April', 'Monitor', 'Elektronik', 20, 3000000, -6.1753, 106.9270),
('Mei', 'Headset', 'Elektronik', 50, 2000000, -6.2298, 106.7852),
('Juni', 'Webcam', 'Elektronik', 35, 1050000, -6.1447, 106.8256),
('Juli', 'SSD', 'Penyimpanan', 25, 3000000, -6.1751, 106.8650),
('Agustus', 'RAM', 'Penyimpanan', 40, 2000000, -6.2088, 106.8456),
('September', 'Router', 'Jaringan', 18, 1800000, -6.1944, 106.8296),
('Oktober', 'Printer', 'Perangkat', 22, 2200000, -6.1753, 106.9270);
