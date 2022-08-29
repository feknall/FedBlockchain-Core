from fl.control_panel import ControlPanel
from flevents import event_listener
from flevents.event_processor import LeadAggregatorEventProcessorR
from rest.gateway_rest_api import GatewayRestApi

gateway_rest_api = GatewayRestApi('http://localhost:8082')
websocket_address = 'ws://localhost:8082'

control_panel = ControlPanel(gateway_rest_api)
personal_info_1, personal_info_2 = control_panel.get_personal_info()
client_index = 1

event_processor = LeadAggregatorEventProcessorR(client_id_1=personal_info_1.clientId,
                                                client_id_2=personal_info_2.clientId,
                                                client_index=client_index,
                                                gateway_rest_api=gateway_rest_api)

event_listener = event_listener.listen(event_processor, websocket_address)

control_panel.has_fl_admin_attribute()
control_panel.get_personal_info()
control_panel.create_model_metadata()
control_panel.start_training()
