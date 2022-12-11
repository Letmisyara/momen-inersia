
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Aplikasi Momen Inersia")
st.subheader("Ini adalah aplikasi sederhana untuk menghitung momen inersia")
st.write("""
dibuat oleh Kelompok 1

*Anggota kelompok:* 
1. Sulung Ismanara Mujianto sebagai Ketua
2. Letmi Syara sebagai anggota
3. Febby Trishe Ananda sebagai anggota
4. Mecca Audynasti Aura sebagai anggota
""")
st.write("""Momen inersia merupakan ukuran kelembaman suatu benda
untuk berputar pada porosnya. 
 """)

tes=st.sidebar.radio("Options",["Home","Perhitungan momen inersia","grafik"])


if tes=="Perhitungan momen inersia": 
    domain=st.sidebar.radio("Perhitungan Momen Inersia",
            ['Batang homogen pusat','Batang homogen ujung',
            'Silinder berongga sumbu','Silinder 2 sumbu',
            'Silinder pejal sumbu','Silinder pejal pusat',
            'Bola pejal pusat','Bola berongga pusat',
            'lempeng tipis pusat','lempeng tipis sumbu'])
    if domain =='Batang homogen pusat':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=1/12
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
    if domain =='Batang homogen ujung':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=1/3
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
    if domain =='Silinder berongga sumbu':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=1
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
    
    if domain=='Silinder 2 sumbu':
        massa = st.slider("massa benda", 0,100)
        jarak1 = st.slider("jarak pertama sumbu putar",0,10)
        jarak2 = st.slider("jarak kedua sumbu putar",0,10)
        k=1/2
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*((jarak1**2)+(jarak2**2))
            st.success(f"momen inersianya adalah {momen_inersia}")
          
    if domain=='Silinder pejal sumbu':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=1/2
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
           
    if domain=='Silinder pejal pusat':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k1=1/4
        k2=1/12
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=(k1*massa*(jarak**2))+(k2*massa*(jarak**2))
            st.success(f"momen inersianya adalah {momen_inersia}")
          
    if domain=='Bola pejal pusat':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=2/5
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
      
    if domain=='Bola berongga pusat':
        massa = st.slider("massa benda", 0,100)
        jarak = st.slider("jarak sumbu putar",0,10)
        k=2/3
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(jarak**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
            
    if domain=='lempeng tipis pusat':
        massa = st.slider("massa benda", 0,100)
        panjang = st.slider("panjang lempeng",0,50)
        lebar=st.slider("lebar lempeng",1,20)
        k=1/12
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*((panjang**2)+(lebar**2))
            st.success(f"momen inersianya adalah {momen_inersia}")
           
    if domain=='lempeng tipis sumbu':
        massa = st.slider("massa benda", 0,100)
        panjang = st.slider("panjang lempeng",0,10)
        k=1/12
        hitung= st.button("Hitung Momen Inersia")
        if hitung:
            momen_inersia=k*massa*(panjang**2)
            st.success(f"momen inersianya adalah {momen_inersia}")
                                                                                    

if tes == "grafik":
    m1=10
    r=np.linspace(0,10,100)
    r1=10
    m=np.linspace(0,1000,100)
        
    I=[]
    fig,ax=plt.subplots(1,2)
    plt.suptitle("Grafik perbandingan hubungan Inersia dengan massa dan jarak")
    for i in range (100):
        I.append(m1*(r[i]**2))

    I2=[]
    for x in range (100):
        I2.append(m[x]*(r1**2))

    
    ax[0].plot(r,I)
    ax[0].set_xlabel("Hubungan jarak dengan inersia")
    ax[1].plot(m,I2)
    ax[1].set_xlabel("Hubungan massa dengan inersia")
    fig.tight_layout()
    plt.show()
    st.pyplot(fig)
