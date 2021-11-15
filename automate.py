import schedule
import time

def job():
    """send mails/backup"""
    print("Sending bulk mails with attachment")

schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10.30").do(job)

if __name__=='__main__':
    while(1):
        schedule.run_pending()
        print('Scheduler is running')
        time.sleep(1)
    

   
