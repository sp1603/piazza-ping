import json
import os
from datetime import datetime
from html2text import HTML2Text
from piazza_api import Piazza
from piazza_api.network import UnreadFilter
from plyer import notification

HTML_2_TEXT = HTML2Text()
HTML_2_TEXT.ignore_links = True

class PiazzaNotifier:
    def __init__(self):
        self.EMAIL = None
        self.PASSWORD = None
        self.NETWORK_IDS = None
        self.CLASS_NAMES = None
        self.notified = set()

    def load_credentials(self):
        if os.path.exists('credentials.json'):
            with open('credentials.json') as f:
                credentials = json.load(f)
                self.EMAIL = credentials.get('email', None)
                self.PASSWORD = credentials.get('password', None)
                self.NETWORK_IDS = credentials.get('network_ids', None)
                self.CLASS_NAMES = credentials.get('class_names', None)

    def compare_dates(self, current_datetime, post_datetime, post_id):
        if post_id not in self.notified and post_datetime > current_datetime:
            self.notified.add(post_id)
            return True
        return False

    def run(self):
        self.load_credentials()
        while True:
            piazza = Piazza()
            piazza.user_login(email=self.EMAIL, password=self.PASSWORD)
            network_ids = self.NETWORK_IDS
 
            class_names = self.CLASS_NAMES
            name = class_names[0]

            for network_id in network_ids:
                unread_filter = UnreadFilter()
                course = piazza.network(network_id)
                unread_posts = course.get_filtered_feed(unread_filter)

                for post in unread_posts['feed']:
                    post_subject = post['subject']
                    post_subject_as_text = HTML_2_TEXT.handle(post_subject).replace('\n', ' ')

                    post_datetime_str = str(post['log'][0]['t'][0:10] + " " + post['log'][0]['t'][11:19])
                    post_datetime_object = datetime.strptime(post_datetime_str, '%Y-%m-%d %H:%M:%S')

                    notify = self.compare_dates(datetime.now(), post_datetime_object, post['id'])

                    if notify:
                        if (network_id == network_ids[1]):
                            name = class_names[1]
                        
                        notification.notify(
                            title= name + " | New Unread Piazza Post",
                            message=post_subject_as_text,
                            app_name="Piazza",
                            app_icon="piazza_icon.ico",
                            timeout=2
                        )

if __name__ == '__main__':
    notifier = PiazzaNotifier()
    notifier.run()
