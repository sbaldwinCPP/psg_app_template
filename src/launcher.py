"""
Put any spin-up code here.
This is currently only used to anchor the 'entry-point' of the app.
powershell script to automatically build the app to an executable points at this file.

"""


from psg_app_template import event_logic

event_logic.run()
