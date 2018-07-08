# data_catcher


What it does:

Creates sqlite db file and receives data from my esp8266 wifi weather station.

This is a simple Python Flask app and uses SqlAlchemy for database access.


To post to the API from the weather station use Arduino code like this example:

Serial.print("connecting to ");
  Serial.println(host);

  String json_msg = String("{\"tmp\" : \"") + temperature + String("\",\"hum\":\"") + h + String("\",\"lux\":\"") + lux + String("\",\"prs\" : \"") + pressure + String("\"}");
   HTTPClient http;    //Declare object of class HTTPClient
   
    http.begin("http://192.168.1.137:5000/record");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
 
    int httpCode = http.POST(json_msg);   //Send the request
    String payload = http.getString();                                        //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection

  Serial.println("closing connection");
  Serial.println();
  Serial.println("Waiting 5 minutes....");

  delay(300000);

I've included my APRX.conf and grab_weather.py script that it calls.  This is how I am posting my weather data to the APRS HAM radio packet network.

See:  

https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System

http://thelifeofkenneth.com/aprx/

