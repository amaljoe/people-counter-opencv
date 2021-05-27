import firebase_admin
from firebase_admin import credentials
from datetime import datetime
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

activity = db.collection('activity')
status = db.collection('status')
store = 2


def enter_store(num):
    activity.add({
        'store': store,
        'number': num,
        'activity': 'enter',
        'time': datetime.now()
    })


def leave_store(num):
    activity.add({
        'store': store,
        'number': num,
        'activity': 'leave',
        'time': datetime.now()
    })


def update_status(num):
    status.document(str(store)).set({
        'store': store,
        'inside': num,
        'time': datetime.now()
    })
