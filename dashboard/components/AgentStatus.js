export default function AgentStatus() {
  return (
    <div style={{
      padding: '20px',
      border: '1px solid #ddd',
      borderRadius: '8px',
      backgroundColor: '#f9f9f9'
    }}>
      <h2>📊 Agent Status</h2>
      <div style={{marginTop: '10px'}}>
        <div><strong>Status:</strong> <span style={{color: 'green'}}>Running</span></div>
        <div><strong>Active Agents:</strong> 1</div>
        <div><strong>Memory:</strong> 256MB</div>
        <div><strong>Uptime:</strong> 0h 0m</div>
      </div>
    </div>
  )
}
