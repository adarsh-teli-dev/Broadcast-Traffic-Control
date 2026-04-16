from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ethernet import ethernet

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet:
        return

    # Ignore malformed packets (fixes DNS error)
    if not isinstance(packet, ethernet):
        return

    # Broadcast detection
    if packet.dst.is_broadcast:
        log.info("Broadcast detected -> Dropping")
        return

    # Normal forwarding
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Broadcast Control Loaded")
