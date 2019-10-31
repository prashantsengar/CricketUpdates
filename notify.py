#notify
import sys
platform_is_windows = sys.platform.startswith('win')
if platform_is_windows:
	from win10toast import ToastNotifier
    def notify(title, msg):
		noti = ToastNotifier()
		noti.show_toast(title, msg, duration=10)
else:
	import subprocess as sc
	def notify(title, msg):
		sc.call(['notify-send', title, msg])
