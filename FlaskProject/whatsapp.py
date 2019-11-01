from yowsup_gateway import YowsupGateway
# from yowsup.layers.axolotl import YowAxolotlLayer
# import logging

# logger.setLevel(logging.DEBUG)

import logging
logger = logging.getLogger('yowsup.stacks.yowstack')
logging.basicConfig(level=logging.DEBUG)

gateway = YowsupGateway(credentials=("08020661647", "password"))

# Send text messages
result = gateway.send_messages([("08065982698", "Delebeat weldone")])


# if result.is_success:
   # print result.inbox, result.outbox

# Receive messages
# result = gateway.receive_messages()
# if result.is_sucess:
   # print result.inbox, result.outbox