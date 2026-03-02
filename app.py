import streamlit as st
from supabase import create_client
import os

# إعدادات الصفحة
st.set_page_config(page_title="Système IGH - Sahel", layout="wide", page_icon="🌍")

# الاتصال بقاعدة البيانات (سيتم جلب المفاتيح من الإعدادات لاحقاً)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

try:
    supabase = create_client(url, key)
except:
    st.error("En attente de configuration des clés...")

# تصميم الواجهة
st.title("🌍 Observatoire Stratégique : Sahel & Afrique")
st.markdown("---")

# جلب البيانات من الجدول
try:
    response = supabase.table("news_table").select("*").order("id", desc=True).execute()
    news_data = response.data

    if news_data:
        for article in news_data:
            with st.expander(f"📌 {article['title']}"):
                st.write(article['description'])
                st.markdown(f"[Lire l'article complet]({article['link']})")
    else:
        st.info("Aucune nouvelle information pour le moment.")
except Exception as e:
    st.warning("Système en cours d'initialisation...")
