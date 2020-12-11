# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import json
import urllib
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime('%m%d%y')
month = "month_" + yesterday[0:2]
day = "day_" + yesterday[2:4]
year = "year_20" + yesterday[4:8]
# month = "month_11"
# day = "day_02"
# year = "year_2016"
# print "MLB Scoreboard for:  " + yesterday[0:2] + "/" + yesterday[2:4] + "/" + yesterday[4:8]
urlbase = "http://gd2.mlb.com/components/game/mlb/"
file = "miniscoreboard.json"
urldate = year + "/" + month + "/" + day + "/"
url = urlbase + urldate + file

response = urllib.urlopen(url)
data = json.loads(response.read())

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("MLB Scoreboard for:  " + yesterday[0:2] + "/" + yesterday[2:4] + "/" + yesterday[4:8] + "\n\n")

        try:
            data["data"]["games"]["game"]
            if not isinstance(data["data"]["games"]["game"], list):
                self.response.write(data["data"]["games"]["game"]["away_team_name"] + "  " + data["data"]["games"]["game"]["away_team_runs"]+ "\n")
                self.response.write(" " + data["data"]["games"]["game"]["away_win"] + "-" + data["data"]["games"]["game"]["away_loss"] + "\n")
                self.response.write(data["data"]["games"]["game"]["home_team_name"] + " " + data["data"]["games"]["game"]["home_team_runs"] + "\n")
                self.response.write(" " + data["data"]["games"]["game"]["home_win"] + "-" + data["data"]["games"]["game"]["home_loss"] + "\n")
            else:
                for obj in data["data"]["games"]["game"]:
                    self.response.write(obj["away_team_name"] + "  " + obj["away_team_runs"] + "\n")
                    self.response.write(" " + obj["away_win"] + "-" + obj["away_loss"] + "\n")
                    self.response.write(obj["home_team_name"] + "  " + obj["home_team_runs"] + "\n")
                    self.response.write(" " + obj["home_win"] + "-" + obj["home_loss"] + "\n")
                    self.response.write("______________________\n")
        except KeyError:
            # self.response.write(data["data"]["games"])
            self.response.write("No Games Yesterday")





app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
