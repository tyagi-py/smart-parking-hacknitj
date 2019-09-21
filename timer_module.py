
# import time
#
#
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         time_format = '{:02d}:{:02d}'.format(mins, secs)
#         print(time_format, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye!\n\n\n\n\n')
#
# countdown(10)
import time
import datetime
def exit_time(hr=0, min=0.5):
    ts = time.time()
    wts = ts + hr * 60 * 60 + min * 60
    return wts


while time.time() < wts:
    # dt_object = datetime.fromtimestamp(wts - time.time())
    # print(dt_object.time())
    print(str(datetime.timedelta(seconds=int(wts - time.time() ) )))



