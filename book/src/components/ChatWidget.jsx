import React, { useState } from 'react';
import './ChatWidget.css';

const ChatWidget = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    {
      text: "Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics course. Ask me anything about the course content!",
      sender: 'bot'
    }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false); // 🔥 icon-first behavior

  const API_BASE_URL = 'http://localhost:8001';

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/chat_with_rag`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });

      let data;
      if (!response.ok) {
        const fallback = await fetch(`${API_BASE_URL}/chat`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: input }),
        });
        data = await fallback.json();
      } else {
        data = await response.json();
      }

      setMessages(prev => [...prev, { text: data.response, sender: 'bot' }]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          text: "⚠️ Backend not reachable. Make sure server is running on port 8001.",
          sender: 'bot'
        }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  /* ================= ICON ONLY ================= */
  if (!isOpen) {
    return (
      <button className="chat-float-button" onClick={() => setIsOpen(true)}>
        🤖
      </button>
    );
  }

  /* ================= CHAT WINDOW ================= */
  return (
    <div className="chat-widget">
      <div className="chat-header">
        <h3>Physical AI Assistant</h3>
        <button
          className="minimize-btn"
          onClick={() => setIsOpen(false)}
        >
          ✕
        </button>
      </div>

      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && (
          <div className="message bot">
            Thinking…
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about Physical AI & Humanoid Robotics..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading}>
          Send
        </button>
      </form>
    </div>
  );
};

export default ChatWidget;
