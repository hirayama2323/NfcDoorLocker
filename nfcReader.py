import nfc


class NfcReader:
    def startup(self):
        print("waiting for new NFC tags...")
        return self

    def connect(self):
        print("Tag: {}".format(str(self)))
        # print("Tag type: {}".format(tag.type))
        # print("{}".format(tag.id))
        # print '\n'.join(tag.dump())
        # if tag.ndef:
        #     print(tag.ndef.message.pretty())
        # return True

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
