import streamlit as st
from supabase import create_client

# الروابط الصحيحة مع تنظيف تلقائي لأي فراغات مخفية
url = "https://bmqjhgassxuxskkldsvu.supabase.co".strip()
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0".strip()

st.title("نظام الأخبار الذكي 📰")

try:
    # إنشاء الاتصال
    supabase = create_client(url, key)
    # جلب البيانات من جدول news
    res = supabase.table("news").select("*").execute()
    
    if res.data:
        for x in res.data:
            st.subheader(x.get('title', 'بدون عنوان'))
            st.write(x.get('content', 'لا يوجد محتوى'))
            st.divider()
    else:
        st.info("تم الاتصال بنجاح ✅ ولكن الجدول لا يحتوي على بيانات حالياً.")
except Exception as e:
    st.error(f"عذراً، لا يزال هناك مشكلة في التعرف على الرابط: {e}")
