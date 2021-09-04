import nfc
import pymysql.cursors


class NfcRegister:
    def startup(self):
        print("waiting for new NFC tags...")
        return self

    def connect(self):
        print("Tag: {}".format(str(self)))

        conn = pymysql.connect(
            user='root',
            passwd='',  # 適宜自分で設定したパスワードに書き換えてください。
            host='127.0.0.1',  # 接続先DBのホスト名或いはIPに書き換えてください。
            db='inhouse_mdb'
        )
        # c = conn.cursor()
        with conn.cursor() as cursor:
            sql = "DELETE FROM NfcId WHERE Idm=(%s)"
            r = cursor.execute(sql, (str(self)))
            print(r)
            # autocommitではないので、明示的にコミットする
        with conn.cursor() as cursor:
            sql = "INSERT INTO NfcId (Idm) VALUES (%s)"
            r = cursor.execute(sql, (str(self)))
            print(r)  # -> 1
            # autocommitではないので、明示的にコミットする
            conn.commit()

    def release(self):
        print("on_release()")
        if self.ndef:
            print(self.ndef.message.pretty())

    clf = nfc.ContactlessFrontend('usb')
    print(clf)
    if clf:
        print("Clf: {}".format(clf))
        clf.connect(rdwr={
            'on-startup': startup,
            'on-connect': connect,
            'on-release': release
        })

    clf.close()
