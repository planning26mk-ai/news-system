import streamlit as st
from supabase import create_client

# هذه هي الروابط الصحيحة المستخرجة من صورك
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"

supabase = create_client(url, key)

st.title("نظام الأخبار الذكي 📰")

try:
    # محاولة جلب البيانات
    res = supabase.table("news").select("*").execute()
    if res.data:
        for x in res.data:
            st.subheader(x.get('title', 'بدون عنوان'))
            st.write(x.get('content', 'لا يوجد محتوى'))
            st.divider()
    else:
        st.info("الاتصال نجح ✅ ولكن الجدول فارغ.")
except Exception as e:
    st.error(f"خطأ: {e}")
