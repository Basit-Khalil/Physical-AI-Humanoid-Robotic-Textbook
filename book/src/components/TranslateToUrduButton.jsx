import React from 'react';

export default function TranslateToUrduButton() {
  return (
    <button
      style={{
        padding: '10px 14px',
        backgroundColor: '#f43f5e',
        color: '#fff',
        border: 'none',
        borderRadius: '6px',
        cursor: 'pointer',
        margin: '12px 0',
      }}
      onClick={() => alert('Failed to translate into Urdu')}
    >
      Translate to Urdu
    </button>
  );
}
