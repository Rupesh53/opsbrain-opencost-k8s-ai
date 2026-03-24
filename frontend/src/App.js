import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const send = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>💸 AI Cost Advisor</h2>
      <input value={query} onChange={(e)=>setQuery(e.target.value)} />
      <button onClick={send}>Ask</button>
      <pre>{response}</pre>
    </div>
  );
}

export default App;
