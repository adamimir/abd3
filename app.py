import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from config import (
    get_all_data,
    get_sales_by_category,
    get_sales_by_month,
    get_locations_data
)

# Set konfigurasi halaman
st.set_page_config(
    page_title="Visualisasi Data Penjualan",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        h1 {
            color: #1f77b4;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.title("📊 Dashboard Visualisasi Data Penjualan")
st.markdown("---")

# Sidebar - Pilih tipe visualisasi
st.sidebar.header("🎨 Pilih Tipe Visualisasi")
chart_type = st.sidebar.selectbox(
    "Pilih Chart:",
    [
        "📈 Pie Chart - Penjualan per Kategori",
        "📊 Bar Chart - Penjualan per Bulan",
        "📉 Line Chart - Tren Penjualan & Profit",
        "🗺️ Map - Lokasi Penjualan",
        "🏔️ Area Chart - Akumulasi Profit"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Gunakan dropdown di atas untuk memilih jenis visualisasi yang ingin ditampilkan.")

# ============================================
# 1. PIE CHART - Penjualan per Kategori
# ============================================
if chart_type == "📈 Pie Chart - Penjualan per Kategori":
    st.subheader("📈 Pie Chart - Penjualan per Kategori")
    
    data = get_sales_by_category()
    
    if data:
        df = pd.DataFrame(data)
        
        fig = px.pie(
            df,
            values='total_penjualan',
            names='kategori',
            title='Distribusi Penjualan per Kategori',
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.3  # Donut chart
        )
        
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabel data
        st.markdown("### 📋 Data Detail")
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Gagal mengambil data dari database")

# ============================================
# 2. BAR CHART - Penjualan per Bulan
# ============================================
elif chart_type == "📊 Bar Chart - Penjualan per Bulan":
    st.subheader("📊 Bar Chart - Penjualan per Bulan")
    
    data = get_sales_by_month()
    
    if data:
        df = pd.DataFrame(data)
        
        fig = px.bar(
            df,
            x='bulan',
            y='total_penjualan',
            title='Total Penjualan per Bulan',
            labels={'bulan': 'Bulan', 'total_penjualan': 'Total Penjualan (Unit)'},
            color='total_penjualan',
            color_continuous_scale='Viridis',
            text='total_penjualan'
        )
        
        fig.update_traces(textposition='outside')
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabel data
        st.markdown("### 📋 Data Detail")
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Gagal mengambil data dari database")

# ============================================
# 3. LINE CHART - Tren Penjualan & Profit
# ============================================
elif chart_type == "📉 Line Chart - Tren Penjualan & Profit":
    st.subheader("📉 Line Chart - Tren Penjualan & Profit")
    
    data = get_sales_by_month()
    
    if data:
        df = pd.DataFrame(data)
        
        fig = go.Figure()
        
        # Tambah line untuk penjualan
        fig.add_trace(go.Scatter(
            x=df['bulan'],
            y=df['total_penjualan'],
            mode='lines+markers',
            name='Total Penjualan',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        
        # Tambah line untuk profit
        fig.add_trace(go.Scatter(
            x=df['bulan'],
            y=df['total_profit'],
            mode='lines+markers',
            name='Total Profit',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=8),
            yaxis='y2'
        ))
        
        fig.update_layout(
            title='Tren Penjualan dan Profit per Bulan',
            xaxis_title='Bulan',
            yaxis=dict(title='Total Penjualan (Unit)'),
            yaxis2=dict(
                title='Total Profit (Rp)',
                overlaying='y',
                side='right'
            ),
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabel data
        st.markdown("### 📋 Data Detail")
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Gagal mengambil data dari database")

# ============================================
# 4. MAP - Lokasi Penjualan
# ============================================
elif chart_type == "🗺️ Map - Lokasi Penjualan":
    st.subheader("🗺️ Map - Lokasi Penjualan")
    
    data = get_locations_data()
    
    if data:
        df = pd.DataFrame(data)
        
        # Konversi ke tipe data yang tepat
        df['latitude'] = df['latitude'].astype(float)
        df['longitude'] = df['longitude'].astype(float)
        df['penjualan'] = df['penjualan'].astype(int)
        
        fig = px.scatter_mapbox(
            df,
            lat='latitude',
            lon='longitude',
            hover_name='produk',
            hover_data={'penjualan': True, 'latitude': ':.4f', 'longitude': ':.4f'},
            color='penjualan',
            size='penjualan',
            color_continuous_scale='Viridis',
            size_max=50,
            title='Lokasi Penjualan Produk',
            mapbox_style='open-street-map',
            zoom=9,
            center=dict(lat=-6.2, lon=106.85)
        )
        
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabel data
        st.markdown("### 📋 Data Detail")
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Gagal mengambil data dari database")

# ============================================
# 5. AREA CHART - Akumulasi Profit
# ============================================
elif chart_type == "🏔️ Area Chart - Akumulasi Profit":
    st.subheader("🏔️ Area Chart - Akumulasi Profit per Kategori")
    
    data = get_all_data()
    
    if data:
        df = pd.DataFrame(data)
        
        # Aggregate by bulan and kategori
        df_area = df.groupby(['bulan', 'kategori']).agg({
            'profit': 'sum'
        }).reset_index()
        
        fig = px.area(
            df_area,
            x='bulan',
            y='profit',
            color='kategori',
            title='Akumulasi Profit per Kategori per Bulan',
            labels={'bulan': 'Bulan', 'profit': 'Profit (Rp)'},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        
        fig.update_layout(
            hovermode='x unified',
            height=500,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabel data
        st.markdown("### 📋 Data Detail")
        st.dataframe(df_area, use_container_width=True)
    else:
        st.error("Gagal mengambil data dari database")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; margin-top: 2rem;'>
    <p>Dashboard Visualisasi Data Penjualan | Praktikum ABD</p>
</div>
""", unsafe_allow_html=True)
