import paho.mqtt.client
import json
import time
import sense_emu
import subprocess

sense = sense_emu.SenseHat()
 
#usuario e senha do dispositivo na plataforma Konkerlabs
usuario_konkerlabs = "nhcc2232kbm7"
senha_konkerlabs = "3FFyUGbGFDKf"
topico_publish1 = "pub/"+usuario_konkerlabs+"/temperatura"
topico_publish2 = "pub/"+usuario_konkerlabs+"/umidade"
topico_publish3 = "pub/"+usuario_konkerlabs+"/pressao"
 
#Funcao: obtem temperatura do emulador
#Parametros: nenhum
#Retorno: temperatura (float)
def temp():    
    temp = str(sense.get_temperature())
    print("[DEBUG] Temperatura: "+str(temp)+" °C")
    return (temp)

#Funcao: obtem umidade do emulador
#Parametros: nenhum
#Retorno: umidade (float)
def umi():    
    umidade = str(sense.get_humidity())
    print("[DEBUG] Umidade: "+str(umidade)+" %")
    return (umidade)

#Funcao: obtem pressao do emulador
#Parametros: nenhum
#Retorno: pressao (float)
def pre():    
    pressao = str(sense.get_pressure())
    print("[DEBUG] Pressão: "+str(pressao)+" mbar")
    return (pressao)
 
#------------------
#Programa principal
#------------------
client = paho.mqtt.client.Client()
client.username_pw_set(usuario_konkerlabs, senha_konkerlabs)
client.connect("mqtt.demo.konkerlabs.net", 1883)
 
while True:
    #obtem os dados
    temperatura = temp()
    umidade = umi()
    pressao = pre()
 
    #envia o valor da temperatura, umidade e pressão para a plataforma Konkerlabs
    payload_json_temp = json.dumps({"temperature": temperatura, "unit": "celsius"})
    client.publish(topico_publish1, payload_json_temp)

    payload_json_umidade = json.dumps({"humidity": umidade, "unit": "%"})
    client.publish(topico_publish2, payload_json_umidade)

    payload_json_pressao = json.dumps({"pressure": pressao, "unit": "mbar"})
    client.publish(topico_publish3, payload_json_pressao)
 
    #aguarda cinco segundos ate a proxima leitura de temperatura do processador
    time.sleep(5)