import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    setLoading(true);

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query })
    });

    const data = await res.json();
    setResponse(data.response);
    setLoading(false);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>💸 AI K8s Cost Advisor</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask about cost optimization..."
        style={{ width: 400, padding: 10 }}
      />

      <button onClick={send} style={{ marginLeft: 10 }}>
        Ask
      </button>

      {loading && <p>Thinking...</p>}

      <pre style={{ marginTop: 20 }}>{response}</pre>
    </div>
  );
}

export default App;