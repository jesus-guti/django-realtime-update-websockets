import { useState, useEffect, useRef } from 'react';


export default function Test(){
  const [val, setVal] = useState(null);
  const ws = useRef(null);

  useEffect(() => {
    const socket = new WebSocket(`ws://${window.location.host}/ws/socket-server/`);

    socket.onopen = () => {
      console.log("opened");
    };

    socket.onclose = () => {
      console.log("closed");
    };

    socket.onmessage = (event) => {
      console.log("got message", event.data);
      setVal(event.data);
    };

    ws.current = socket;

    return () => {
      socket.close();
    };
  }, []);

  return <div>Value: {val}</div>;
};