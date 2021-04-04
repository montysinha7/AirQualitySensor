import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import time


conn_str = "IoT Device Conn String HERE"
MSG_SND = '{{"messageId": 100,"deviceId": "Raspberry Pi Web Client","temperature": {temperature},"humidity": {humidity}}}' 
while True:
    
    def iothub_client_init():  
        client = IoTHubDeviceClient.create_from_connection_string(conn_str)  
        return client  
    async def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True:  
                await client.connect()
                msg_txt_formatted = MSG_SND.format(temperature=35, humidity=30)  
                message = msg_txt_formatted
                print( "Sending message: {}".format(message) )  
                await client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)
                await client.disconnect()
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        asyncio.run(iothub_client_telemetry_sample_run())
