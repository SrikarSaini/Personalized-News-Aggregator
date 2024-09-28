import os
import sys
import django
import csv

project_path = 'D:/SRIKAR/STUDY/DJANGO/DeepKlarity/Assignment/'
sys.path.insert(0, project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = "Assignment.settings"

django.setup()

from News.models import Article

def load_articles_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            article = Article(
                title=row['title'],
                summary=row['summary'],
                publication_date=row['publication_date'],
                source=row['source'],
                url=row['url'],
                category=row['Category']
            )
            article.save()

if __name__ == "__main__":
    load_articles_from_csv(r"D:\SRIKAR\STUDY\DJANGO\DeepKlarity\Assignment\Scripts\news_articles.csv")
    print("Articles loaded into the database successfully.")
