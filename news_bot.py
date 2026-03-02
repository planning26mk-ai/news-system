import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client

# جلب المفاتيح من الخزنة التي أعددتِها
URL = os.environ.get("SUPABASE_URL")
KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(URL, KEY)

def fetch_news():
    # مصادر الأخبار التي طلبها المدير
    SOURCES = {
        "Jeune Afrique": "https://www.jeuneafrique.com/feed/",
        "TSA Algerie": "https://www.tsa-algerie.com/feed/",
        "Maliweb": "https://www.maliweb.net/feed"
    }
    
    all_news = []
    print("📡 جاري جمع أخبار أفريقيا والساحل...")

    for name, rss_url in SOURCES.items():
        try:
            r = requests.get(rss_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
            soup = BeautifulSoup(r.content, 'xml')
            items = soup.find_all('item')[:5]
            
            for item in items:
                all_news.append({
                    "title": item.title.text.strip(),
                    "link": item.link.text.strip(),
                    "description": item.description.text[:250].strip() if item.description else ""
                })
        except:
            print(f"❌ فشل سحب أخبار {name}")

    if all_news:
        # إرسال البيانات لجدول news_table
        supabase.table("news_table").insert(all_news).execute()
        print(f"✅ تم تحديث {len(all_news)} خبراً!")

if __name__ == "__main__":
    fetch_news()
