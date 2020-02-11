//alert('hola')// muestra mensaje en la ventana

var etiqueta;
function onloadFcn(){
	etiqueta=document.getElementById("led");
	etiqueta.innerHTML = "led 1"
}
	
	
  //<!-- este script tiene que abrirse y cerrarse-->

  // Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("tailor.cloudmqtt.com", 30143, "web_" + parseInt(Math.random() * 100, 10));
  //<!-- dentro del parentecis tengo el url y el puerto ws o websocket, luego solo genera un numero aleatorio de inicio de secion-->
  // set callback handlers
  //<!-- VAMOS ASOCIAS LOS EVENTOS, cuando se pierda la conexion sate a la funcion despues del igual-->
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  //<!-- los corchetes el variables de diccionario, en esta parte actualiazmos con nuestros credednciales-->
  var options = {
    useSSL: true,
    userName: "tnshttbl",
    password: "xYvqXagwmhXP",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
  topic_rx="test";//<!-- para que reciba la rasbpherry, si me suscribo al mismo topico voy a recibir-->
  topic_tx="led";
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
	//<<!---- es lo mismo que el printt
	
    client.subscribe(topic_rx);//<!-- para suscribir a un evento-->
    message = new Paho.MQTT.Message("ll:Hello: CloudMQTT");
    message.destinationName = topic_tx;//<!-- qui se pone todo lo que se vaya a pubicar
    
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    console.log("el mensaje fue:"+message.payloadString); //aqui recibe todo
	accion(message.payloadString)
	
  }
  
    // called when a message arrives
  function sendMessage(msg) {
    message = new Paho.MQTT.Message(msg);
    message.destinationName = topic_tx;
    client.send(message);
	
  }

    // called when a message arrives
  function ledOn() {
	sendMessage('led=1')	
  }
  function ledOff() {
	sendMessage('led=0')	
  }
 
  function accion(msg){ //
	 mensaje=msg.split('=');
	/* if(mensaje[0]=='i')
		 document.getElementById('sensor_i').innerHTML=mensaje[1];
	 if(mensaje[0]=='p')
		 document.getElementById('sensor_p').innerHTML=mensaje[1];
	 if(mensaje[0]=='l')
		 document.getElementById('sensor_l').innerHTML=mensaje[1];*/
  }
  
 // t=22
 // p=1 / 0
  //l=1 / 0
  