from MyPublisher import MyPublisher
import time
import json

if __name__ == "__main__":
    test = MyPublisher("TestPublisher2")
    test.start()

    endInput = '1'
    while endInput != "end":
        timenow = time.ctime()
        payload = {}
        if endInput == '1':
            payload = {"chat_ID": 1, "location": {"latitude": 45.03, "longitude": 7.62}, "status": "closed", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/1/notifications", json.dumps(payload))
        elif endInput == '2':
            payload = {"chat_ID": 1, "location": {"latitude": 45.03, "longitude": 7.62}, "status": "open", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/1/notifications", json.dumps(payload))
        elif endInput == '3':
            payload = {"chat_ID": 1, "location": {"latitude": 45.08, "longitude": 7.68}, "status": "open", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/1/notifications", json.dumps(payload))
        elif endInput == '4':
            payload = {"chat_ID": 2, "location": {"latitude": 45.03, "longitude": 7.62}, "status": "open", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/2/notifications", json.dumps(payload))
        elif endInput == '5':
            payload = {"chat_ID": 2, "location": {"latitude": 45.03, "longitude": 7.62}, "status": "closed", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/2/notifications", json.dumps(payload))
        elif endInput == '6':
            payload = {"chat_ID": 459592011, "location": {"latitude": 45.03, "longitude": 7.62}, "status": "closed", "timestamp": str(timenow)}
            test.mqtt_client.myPublish("/Turin/459592011/notifications", json.dumps(payload))
        else:
            payload = {"invalid": True}
            test.mqtt_client.myPublish("/Turin/0/notifications/", json.dumps(payload)) 

        print("Publishing: '%s'" % (payload))  
        endInput = input()

    test.stop()
