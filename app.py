import streamlit as st
from supabase import create_client

# محاولة الاتصال برابط بديل وتنسيق أبسط
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"

st.title("لوحة تحكم الأخبار")

try:
    # إنشاء الاتصال
    supabase = create_client(url, key)
    # جلب البيانات
    data = supabase.table("news").select("*").execute()
    
    if data.data:
        for row in data.data:
            st.write(f"### {row.get('title', 'عنوان غير متوفر')}")
            st.write(row.get('content', 'لا يوجد محتوى'))
            st.markdown(f"[رابط المصدر]({row.get('link', '#')})")
            st.divider()
    else:
        st.info("الاتصال ناجح، ولكن الجدول فارغ حالياً.")

except Exception as e:
    st.error(f"عذراً، لا يزال هناك مشكلة في الربط: {e}")
    st.info("نصيحة: تأكدي من أن مشروع Supabase ليس في وضع 'Pause' أو معطل.")
