import React from 'react';

export default function PersonalizeContentButton() {
  return (
    <button
      style={{
        padding: '10px 14px',
        backgroundColor: '#25c2a0',
        color: '#fff',
        border: 'none',
        borderRadius: '6px',
        cursor: 'pointer',
        margin: '12px 0',
      }}
      onClick={() => alert('Personalization coming soon 🚀')}
    >
      Personalize Content
    </button>
  );
}
