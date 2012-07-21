from wmd.actions import Action

import settings

class IdentWithNickserv(Action):
    def __init__(self):
        self.logged_in = False

    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()
        msg = obj_data.params
        if username and username.lower() == 'nickserv':

            if 'identify' in msg.lower()\
            and not self.logged_in:
                msg = 'identify %s' % (settings.NICKSERV_PASSWORD)
                print "%s: Logging in..." % self.__class__.__name__
                irc.privmsg(username, msg)
                self.logged_in = True
            elif 'are now identified' in msg.lower():
                print "%s: Logged in." % (self.__class__.__name__)