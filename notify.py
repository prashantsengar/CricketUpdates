#notify the thing

from win10toast import ToastNotifier

def notify(msg, title="Cricket Update"):
    noti = ToastNotifier()
    noti.show_toast(title, msg, duration=10)
