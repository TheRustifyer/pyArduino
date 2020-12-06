//Libraries
#include <DHT.h>
#include <LiquidCrystal.h>

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)

DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup(){
   lcd.begin(16, 2);               // Inicializamos la pantalla LCD
   Serial.begin(9600);             // Inicializamos el puerto serie
   Serial.setTimeout(100);         // Reducimos el timeout del puerto serie para reducir el lag, quizás querais ajustarlo
   dht.begin();
}

void loop(){
  // En caso de que se haya recibido algo por el puerto serie
    //Read data and store it to variables hum and temp

    //Print temp and humidity values to serial monitor   
  if (Serial.available()) {                        
    String buff = Serial.readString();                              
    if (buff == "clear_lcd") {
      // Si recibimos la orden "clear_lcd" borramos la pantalla
      lcd.clear();                                                  
    } 
    else if (buff == "read_buff") {
      hum = dht.readHumidity();
      temp= dht.readTemperature();
      Serial.print("Humedad: ");
      Serial.print(hum);
      Serial.print(" %, Temp --> ");
      Serial.print(temp);
      Serial.println(" C");

    }
    else {
      // Localizamos el separador ","
      int commaIndex = buff.indexOf(',');  
      // Extraemos el mensaje a imprimir                         
      String message = buff.substring(0,commaIndex);    
      // Extraemos la linea en que queremos escribir el mensaje             
      int lcd_line = buff.substring(commaIndex+1).toInt();   
      // Movemos el cursor a la linea que deseamos       
      lcd.setCursor(0,lcd_line);   
      // Imprimimos el mensaje                                 
      lcd.print(message);                                           
    }
  }
}
