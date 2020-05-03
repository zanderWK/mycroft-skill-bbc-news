# mycroft-skill-bbc-news

#

# A Mycroft skill to play the latest bbc news

#

# Based on the daily_meditation skill by kfezer and cbc-news by chrison999

#

# Modified by WalterKlosse

#

# This skill is licensed under the GNU General Public License v3.

# You should have received a copy of the GNU General Public License

# along with this skill.  If not, see <http://www.gnu.org/licenses/>.





import feedparser

import time

from os.path import dirname

import re



from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill

from mycroft.util import play_mp3

from mycroft.util.log import getLogger



__author__ = 'WalterKlosse'



LOGGER = getLogger(__name__)





class BBCNewsSkill(MycroftSkill):

    def __init__(self):

        super(EWNNewsSkill, self).__init__(name="EWNNewsSkill")

        self.process = None



    def initialize(self):

        intent = IntentBuilder("EWNNewsIntent").require(

            "EWNNewsKeyword").build()

        self.register_intent(intent, self.handle_intent)



    def handle_intent(self, message):

        try:



            data = feedparser.parse("http://ewn.co.za/RSS%20Feeds/Latest%20News.xml")

            self.speak_dialog('EWN.news')

            time.sleep(5)



            self.process = play_mp3(

                re.sub(

                    'https', 'http', data['entries'][0]['links'][0]['href']))



        except Exception as e:

            LOGGER.error("Error: {0}".format(e))



    def stop(self):

        if self.process and self.process.poll() is None:

            self.speak_dialog('EWN.news.stop')

            self.process.terminate()

            self.process.wait()





def create_skill():

    return BBCNewsSkill()
