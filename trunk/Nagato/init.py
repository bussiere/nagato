from ZODB import FileStorage, DB 
import transaction

storage = FileStorage.FileStorage('bd/id.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
if not root.has_key('userdb2'):
    from BTrees.OOBTree import OOBTree
    root['userdb'] = OOBTree()

userdb = root['userdb']
userdb[0] = 0
transaction.commit()
print userdb.items()
k = userdb.items()
print len(k)
connection.close()