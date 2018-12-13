import urllib
import json
import time
status= "0"
while True:

    
    response = urllib.urlopen("https://greatastha.000webhostapp.com/data/getstatus1.php");


       data = response.read()


       textjson = data.decode("utf-8")


      dic = json.loads(textjson)

      print(dic)


     ustatus = dic[0]["status"]

    
  print(ustatus)

     time.sleep(1)

    
'''if status != ustatus:

        status = ustatus
  
        print('status : '+status)
  
       if status == "1":
 
           led.on()
        
       else:
            
           led.off()'''
