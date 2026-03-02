import streamlit as st
from supabase import create_client

# الروابط المباشرة
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"
supabase = create_client(url, key)

st.title("نظام الأخبار الذكي 📰")

try:
    # نحاول جلب البيانات من جدول news (جربي تغيير الاسم هنا إذا لزم الأمر)
    response = supabase.table("news").select("*").execute()
    
    if response.data and len(response.data) > 0:
        for item in response.data:
            st.subheader(item.get('title', 'خبر جديد'))
            st.write(item.get('content', 'لا يوجد تفاصيل'))
            st.markdown(f"[رابط الخبر]({item.get('link', '#')})")
            st.divider()
    else:
        st.info("الاتصال ناجح ✅ ولكن لم يتم العثور على بيانات داخل الجدول. تأكدي من إضافة أسطر في Supabase.")

except Exception as e:
    st.error(f"خطأ: {e}")
