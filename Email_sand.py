import smtplib, time
from email.message import EmailMessage

last_time = None
title_num = 0
def sand_Email(Subject):
    global title_num
    global last_time
    if last_time != None and time.time() - last_time < 5:
        print("60초가 지나지 않았습니다.")
        return
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.starttls()
    email_id = 'dydwn1332@naver.com'
    email_pass = 'qprk154712@'

    smtp.login(email_id, email_pass)
    message = EmailMessage()
    message.set_content('test')
    message["Subject"] = Subject + str(title_num)
    message["From"] = email_id
    message["To"] = email_id
    smtp.send_message(message)
    smtp.quit()
    last_time = time.time()
    print("이메일이 성공적으로 보내졌습니다.")
    title_num += 1
    print(last_time)
    print(time.time())