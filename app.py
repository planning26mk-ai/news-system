import streamlit as st
from supabase import create_client

# الروابط المستخرجة بدقة من صورك
URL = "https://bmqjhgassxuxskkldsvu.supabase.co"
KEY = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"

st.title("نظام الأخبار الذكي 📰")

try:
    # إنشاء الاتصال
    supabase = create_client(URL, KEY)
    
    # محاولة جلب البيانات من جدول news
    # ملاحظة: إذا ظهرت الصفحة بيضاء، تأكدي من إضافة بيانات في جدول news داخل Supabase
    res = supabase.table("news").select("*").execute()
    
    if res.data:
        for item in res.data:
            st.subheader(item.get('title', 'عنوان الخبر'))
            st.write(item.get('content', 'محتوى الخبر'))
            st.divider()
    else:
        st.info("✅ الاتصال ناجح، ولكن لا توجد بيانات في الجدول حالياً.")

except Exception as e:
    st.error(f"مشكلة تقنية: {e}")
