# data_catcher

Create sqlite db file and receives data from my esp8266 wifi weather station.

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



