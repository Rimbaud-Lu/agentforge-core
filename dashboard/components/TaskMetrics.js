export default function TaskMetrics() {
  return (
    <div style={{
      padding: '20px',
      border: '1px solid #ddd',
      borderRadius: '8px',
      backgroundColor: '#f9f9f9'
    }}>
      <h2>📈 Task Metrics</h2>
      <div style={{marginTop: '10px'}}>
        <div><strong>Tasks Total:</strong> 0</div>
        <div><strong>Skills Called:</strong> 0</div>
        <div><strong>Errors:</strong> 0</div>
        <div><strong>Avg Latency:</strong> 0ms</div>
      </div>
      <p style={{marginTop: '10px', fontSize: '12px', color: '#666'}}>
        Metrics collected from Prometheus
      </p>
    </div>
  )
}
