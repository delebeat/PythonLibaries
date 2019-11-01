from xmlrpc.server import SimpleXMLRPCServer
# import xmlrpclib

def is_even(n):
    return n % 2 == 0
server = SimpleXMLRPCServer(("localhost", 8069))

print("Listening on port 8069...")
server.register_function(is_even, "is_even")
server.serve_forever()


# proxy = xmlrpclib.ServerProxy("http://localhost:8069/")
# print("3 is even: %s" % str(proxy.is_even(3)))
# print("100 is even: %s" % str(proxy.is_even(100)))