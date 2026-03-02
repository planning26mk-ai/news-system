import streamlit as st
from supabase import create_client

# الروابط المباشرة (تأكدنا أنها تعمل لأن الخطأ الأحمر اختفى)
url = "https://bmqjhgassxuxskkldsvu.supabase.co"
key = "sb_publishable_EyqvcYQadom5V0EqmJQ1Q_joKwp3I0"
supabase = create_client(url, key)

st.title("فحص نظام الأخبار 🔍")

try:
    # 1. محاولة جلب أسماء الجداول المتاحة (لنتأكد من الاسم)
    st.write("يتم الآن فحص قاعدة البيانات...")
    
    # 2. جلب البيانات من جدول news
    # ملاحظة: جربي تغيير "news" إلى "NEWS" هنا إذا لم تظهر نتيجة
    response = supabase.table("news").select("*").execute()
    
    if response.data:
        st.success(f"✅ وجدنا {len(response.data)} خبر!")
        for item in response.data:
            st.subheader(item.get('title', 'عنوان مفقود'))
            st.write(item.get('content', 'محتوى مفقود'))
            st.divider()
    else:
        st.warning("⚠️ الاتصال ناجح، ولكن الجدول 'news' فارغ تماماً. هل أنتِ متأكدة من وجود بيانات بداخله؟")

except Exception as e:
    st.error(f"❌ خطأ تقني: {e}")
