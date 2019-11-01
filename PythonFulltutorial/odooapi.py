import xmlrpclib

root = 'http://%s:%d/xmlrpc/' % ('68.183.191.88', 8069)

uid = xmlrpclib.ServerProxy(root + 'common').login('facility', 'admin', 'admin')
# print "Logged in as %s (uid: %d)" % ('admin', uid)

# Create a new note
sock = xmlrpclib.ServerProxy(root + 'object')
args = {
    'name' : 'Delebeat',

}
# print(args)
note_id = sock.execute('facility', 'admin', 'admin',uid, 'res.partner', 'create', args)

# models.execute_kw(db, uid, password,
#     'res.partner', 'search',
#     [[['is_company', '=', True], ['customer', '=', True]]])



# print(note_id)

# sock = xmlrpclib.ServerProxy(root + 'object')
# args = {
#     'color' : 8,
#     'memo' : 'This is a note',
#     'create_uid': uid,
# }
# note_id = sock.execute(uid, 'note.note', 'create', args)