import time
import s7MingfengLib
import DBTables
import requests
import json
import os
#plc read sampling time [sec]:
ts_plc_update       =    2
#ip upload sampling time [sec]:
ts_ip_update        =    5
# reboot sampling time [sec]:
ts_reboot   =    2
#  s71500 rack number:
rackNo   =    0
#  s71500 slot number:
slotNo   =    1
#  s71500 device number:
deviceNr =    2
# s71500 ip adress:
PLC_IP   =    '169.254.12.77'
# cloud server adress:
mqtthost =    "88.99.24.40"
# cloud server port:
mqttport =    1883
# topics definition
topic1   =    "Simcheng/3002/scy1"
topic2   =    "Simcheng/3002/scy2"
topic3   =    "Simcheng/3002/scy3"
# client name:
clientname = "simchengProducer"
# client user name:
username   = "simcheng"
# client password:
password   = "Simcheng2020"
mqttport =    1883
# topics definition
# topic1   =    "Mingfeng/3003/scy1"
# topic2   =    "Mingfeng/3003/scy2"
# topic3   =    "Mingfeng/3003/scy3"
# # client name:
# clientname = "mingfengConsumer"
# # client user name:
# username   = "simcheng"
# # client password:
# password   = "Simcheng2020"
### IP upload Parameters ###
organId = 2002
devId   = "3001"            # device ID
api_ip_upload = 'user'      # user name
api_password  = 'user'      # password

auth_url = "http://88.99.24.40:8088/api/auth/signin";
optIn_url = "http://88.99.24.40:8088/api/optIn";
  
def step_fun_plc():
    try:
        plc =s7MingfengLib.plcConnect(PLC_IP,rackNo,slotNo)
        DBIdNo,Data = s7MingfengLib.ReadAllDBs(plc,DBTables.DBIDs)
        scy1_Ids,scy1_data =s7MingfengLib.readIDs(DBTables.DBIDs,Data,1)
        scy2_Ids,scy2_data =s7MingfengLib.readIDs(DBTables.DBIDs,Data,2)
        scy3_Ids,scy3_data =s7MingfengLib.readIDs(DBTables.DBIDs,Data,3)
        #print(scy1_data)
        s7MingfengLib.on_publish(mqttClient,topic1,s7MingfengLib.Convert2SimchengForm(scy1_Ids, scy1_data) , 1)
        s7MingfengLib.on_publish(mqttClient,topic2,s7MingfengLib.Convert2SimchengForm(scy2_Ids, scy2_data) , 1)
        s7MingfengLib.on_publish(mqttClient,topic3,s7MingfengLib.Convert2SimchengForm(scy3_Ids, scy3_data) , 1)
    except:
        print("please check the ethernet connection")

     
def step_fun_upload_ip():
    try:
        ipadr = s7MingfengLib.get_ip()
       # ngrok_adr = s7XinyingLib.get_ngrok_url()
        s7MingfengLib.ip_upload(auth_url,optIn_url,api_ip_upload,api_password,organId,devId,ipadr,ipadr)
    except:
        print("upload ip failed")
    #ip_upload(auth_url,optIn_url,api_ip_upload,api_password,organId,devId,ipadr)
     
def step_fun_reboot():
    print ("reboot ...")
    os.system('sudo reboot')




if __name__ == "__main__":
    mqttClient = s7MingfengLib.on_mqtt_connect(mqtthost,mqttport,clientname,username,password)
    sched = s7MingfengLib.task_scheduler()
    sched.add_job(step_fun_plc, 'cron', second='*/'+str(ts_plc_update),hour='*',max_instances = int(1e25))
    sched.add_job(step_fun_upload_ip, 'cron', second='*/'+str(ts_ip_update),hour='*',max_instances = int(1e25))
    sched.add_job(step_fun_reboot, 'cron', minute='*/'+str(ts_reboot),hour='*',max_instances = int(1e25))
    sched.start()
