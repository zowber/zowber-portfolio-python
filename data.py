import os
from dotenv import load_dotenv

from pymongo import MongoClient
from datastructures import CaseStudy


load_dotenv()

# FIXME: .env
client = MongoClient(os.getenv('DB_HOST'))

db = client['portfolioitems']
collection = db['casestudies']
documents = collection.find()

#for document in documents:
#    print(document)

case_studies = [CaseStudy(doc['id'], doc['name'], doc['description'], doc['lead'], doc['heroImgUrl'], doc['heroImgRawUrl'], doc['labels'], doc['meta'], doc['sections']) for doc in documents]

for case_study in case_studies:
    print("Number of labels: ", len(case_study.labels))