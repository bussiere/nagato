from ZODB import FileStorage, DB 
import transaction

storage = FileStorage.FileStorage('bd/id.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
root[0] = 0
transaction.commit()
print root.items()
k = root.items()
print len(k)
connection.close()