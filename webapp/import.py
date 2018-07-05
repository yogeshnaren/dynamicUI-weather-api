import csv
import django
import datetime
import sys, os
from models import weather
from django.core.management import setup_environ
from .. import settings

project_dir = "/Users/yogeshnaren/Learning/UC Masters in Data Science/Spring 2018/Cloud Computing/Project/Assignment II - RESTful API/Weather_Forecast"
csv_filepathname="/Users/yogeshnaren/Learning/UC Masters in Data Science/Spring 2018/Cloud Computing/Project/Assignment II - RESTful API/Weather_Forecast/webapp/daily.csv"

sys.path.append(project_dir)

settings.configure()
os.environ['DJANGO_SETTINGS_MODULE'] = 'webapp.settings'
django.setup()

data = csv.reader(open(csv_filepathname))
for row in data:
	if row[0] != 'DATE' :
		post = weather()
		post.date = row[0]
		post.tmax = row[1]
		post.tmin = row[2]
		post.save()


# with open('some/path/to/file.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     header = next(reader)
#     Foo.objects.bulk_create([Foo(first_name=row[0], last_name=row[1]) for row in reader])