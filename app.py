import streamlit as st
from supabase import create_client

# جلب البيانات من Secrets التي وضعتِها
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("نظام الأخبار الذكي")

# جلب الأخبار من جدول news
try:
    response = supabase.table("news").select("*").execute()
    news_list = response.data

    for news in news_list:
        st.subheader(news['title'])
        st.write(news['content'])
        st.write(f"[رابط الخبر]({news['link']})")
        st.divider()
except Exception as e:
    st.error(f"حدث خطأ في الاتصال: {e}")
