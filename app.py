import streamlit as st
from supabase import create_client

# تم نسخ الرابط والمفتاح مباشرة من صورك لضمان الدقة
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"

st.set_page_config(page_title="نظام الأخبار الذكي", layout="centered")
st.title("نظام الأخبار الذكي 📰")

try:
    supabase = create_client(url, key)
    # جلب البيانات من جدول news
    response = supabase.table("news").select("*").execute()
    
    if response.data:
        for item in response.data:
            st.subheader(item.get('title', 'عنوان الخبر'))
            st.write(item.get('content', 'لا يوجد تفاصيل'))
            st.divider()
    else:
        st.info("الاتصال ناجح ✅ ولكن الجدول لا يحتوي على بيانات حالياً.")

except Exception as e:
    st.error(f"مشكلة تقنية: {e}")
