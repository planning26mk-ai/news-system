import streamlit as st
from supabase import create_client

# وضعنا الروابط هنا مباشرة لنتخلص من مشكلة الـ Secrets
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"
supabase = create_client(url, key)

st.title("نظام الأخبار الذكي")

try:
    # جلب البيانات من جدول news
    response = supabase.table("news").select("*").execute()
    news_list = response.data

    if not news_list:
        st.info("لا توجد أخبار حالياً في القاعدة.")
    else:
        for news in news_list:
            st.subheader(news.get('title', 'بدون عنوان'))
            st.write(news.get('content', 'لا يوجد محتوى'))
            if news.get('link'):
                st.write(f"[رابط الخبر]({news['link']})")
            st.divider()
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
