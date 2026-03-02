import streamlit as st
from supabase import create_client

import streamlit as st
from supabase import create_client

# تأكدي أن السطر يبدأ وينتهي بعلامة "
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"

supabase = create_client(url, key)

st.title("نظام الأخبار 📰")

try:
    # جلب البيانات - تأكدي أن اسم الجدول news بحروف صغيرة
    data = supabase.table("news").select("*").execute()
    if data.data:
        for item in data.data:
            st.subheader(item.get('title'))
            st.write(item.get('content'))
            st.divider()
    else:
        st.info("الاتصال سليم ولكن الجدول فارغ.")
except Exception as e:
    st.error(f"يرجى التحقق من الرابط في Supabase: {e}")
